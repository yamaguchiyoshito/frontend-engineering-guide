<script setup lang="ts">
import { onMounted, reactive, computed, ref } from 'vue'
import { withBase } from 'vitepress'
import items from '../../../build/checklist-items.json'

/** Team checklist answers (DX Criteria scoring: はい 1, でも 0.5, いいえ 0; anti-patterns reversed), kept in this browser's localStorage only. */
const props = defineProps<{ summary?: boolean }>()
const KEY = 'fe-guide.team-assessment.v1'
type Answer = 'yes' | 'yes-but' | 'no-but' | 'no'
type Item = (typeof items)[number]
type Entry = { answer?: Answer; note: string }
const OPTIONS: { v: Answer; label: string }[] = [{ v: 'yes', label: 'はい' }, { v: 'yes-but', label: 'はい、でも…' }, { v: 'no-but', label: 'いいえ、でも…' }, { v: 'no', label: 'いいえ' }]
const byId: Record<string, Item> = Object.fromEntries(items.map(i => [i.sid, i]))
const state = reactive<{ items: Record<string, Entry>; updatedAt: string | null; ready: boolean }>({ items: {}, updatedAt: null, ready: false })
const slots = ref<{ sid: string; el: HTMLElement }[]>([])
const sub = ref<string | null>(null) // the sub-theme of the current page (page mode)
const copied = ref(false)

function load() {
  try {
    const raw = localStorage.getItem(KEY); if (!raw) return
    const data = JSON.parse(raw)
    if (data && typeof data === 'object' && data.items) {
      for (const [sid, e] of Object.entries<any>(data.items)) {
        if (!byId[sid] || !e || typeof e !== 'object') continue
        const answer = OPTIONS.some(o => o.v === e.answer) ? e.answer as Answer : undefined
        const note = typeof e.note === 'string' ? e.note : ''
        if (answer || note) state.items[sid] = { answer, note }
      }
      state.updatedAt = typeof data.updatedAt === 'string' ? data.updatedAt : null
    }
  } catch { /* blocked storage: the page still works, nothing persists */ }
}
function save() {
  state.updatedAt = new Date().toISOString().slice(0, 10)
  try { localStorage.setItem(KEY, JSON.stringify({ version: 1, updatedAt: state.updatedAt, items: state.items })) } catch { /* ignore */ }
}
function entry(sid: string): Entry { return state.items[sid] ?? { note: '' } }
function score(sid: string, answer = entry(sid).answer): number | null {
  if (!answer) return null
  const base = answer === 'yes' ? 1 : answer === 'no' ? 0 : 0.5
  return byId[sid].antipattern ? 1 - base : base
}
function setAnswer(sid: string, v: Answer) {
  const e = entry(sid); const answer = e.answer === v ? undefined : v
  if (!answer && !e.note) delete state.items[sid]; else state.items[sid] = { answer, note: e.note }
  save()
}
function setNote(sid: string, note: string) {
  const e = entry(sid)
  if (!note && !e.answer) delete state.items[sid]; else state.items[sid] = { answer: e.answer, note }
  save()
}
function clear(sids: string[]) {
  const label = props.summary ? 'チームチェック全体' : 'この小テーマ'
  if (!confirm(`この端末に保存した${label}の回答と評価記述を消します。よろしいですか？`)) return
  for (const sid of sids) delete state.items[sid]
  save()
}
const fmt = (n: number) => (Number.isInteger(n) ? String(n) : n.toFixed(1))
function stats(list: Item[]) {
  const answered = list.filter(i => entry(i.sid).answer).length
  const points = list.reduce((sum, i) => sum + (score(i.sid) ?? 0), 0)
  return { total: list.length, answered, points }
}
const pageItems = computed(() => items.filter(i => i.sub === sub.value))
const pageStats = computed(() => stats(pageItems.value))
const allStats = computed(() => stats(items))
const themes = computed(() => [...new Set(items.map(i => i.theme))].map(theme => {
  const list = items.filter(i => i.theme === theme)
  const subs = [...new Set(list.map(i => i.sub))].map(s => { const l = list.filter(i => i.sub === s); return { sub: s, subtitle: l[0].subtitle, path: l[0].path, ...stats(l) } })
  return { theme, ...stats(list), subs }
}))
const tally = (st: { points: number; answered: number; total: number }) => `得点 ${fmt(st.points)} / ${st.total}、回答 ${st.answered} / ${st.total}`
/** Per-theme and per-sub-theme sections with their tallies, then the items. Summary mode nests sub-themes under their theme. */
function markdownFor(list: Item[], withThemes: boolean) {
  const lines: string[] = []
  for (const theme of [...new Set(list.map(i => i.theme))]) {
    const tl = list.filter(i => i.theme === theme)
    if (withThemes) lines.push(`## ${theme}（${tally(stats(tl))}）`, '')
    for (const s of [...new Set(tl.map(i => i.sub))]) {
      const l = tl.filter(i => i.sub === s)
      lines.push(`${withThemes ? '###' : '##'} ${s} ${l[0].subtitle}（${tally(stats(l))}）`, '')
      for (const i of l) {
        const e = entry(i.sid); const sc = score(i.sid); const label = OPTIONS.find(o => o.v === e.answer)?.label
        lines.push(`- ${i.sid} ${i.perspective}${i.antipattern ? '（アンチパターン：配点逆転）' : ''}：${label ? `${label}（${fmt(sc!)}点）` : '未回答'}`, `  項目文：${i.criterion}`, `  評価記述：${e.note || '（未記入）'}`)
      }
      lines.push('')
    }
  }
  return lines.join('\n')
}
const markdown = computed(() => {
  const list = props.summary ? items : pageItems.value; const st = props.summary ? allStats.value : pageStats.value
  const head = [`# チームチェックの回答（${state.updatedAt ?? '未記録'}）`, '', `${tally(st)}。配点は出典の「使い方」に従い、はい 1点、はい・いいえでも… 0.5点、いいえ 0点、アンチパターンは逆転。`, '']
  if (props.summary) { // per-theme tally (same figures as the on-page table) before the per-item lines
    head.push('| 大テーマ | 回答済み | 得点 |', '| :--- | ---: | ---: |')
    for (const t of themes.value) head.push(`| ${t.theme} | ${t.answered} / ${t.total} | ${fmt(t.points)} / ${t.total} |`)
    head.push(`| 合計 | ${st.answered} / ${st.total} | ${fmt(st.points)} / ${st.total} |`, '')
  }
  return head.join('\n') + markdownFor(list, !!props.summary)
})
async function copy() {
  try { await navigator.clipboard.writeText(markdown.value); copied.value = true; setTimeout(() => (copied.value = false), 2000) } catch { copied.value = false }
}

onMounted(() => {
  load()
  const found: { sid: string; el: HTMLElement }[] = []
  for (const heading of Array.from(document.querySelectorAll<HTMLHeadingElement>('.vp-doc h2, .vp-doc h3, .vp-doc h4'))) {
    const m = /^(\d-\d-\d)：/.exec(heading.textContent?.trim() ?? '')
    if (!m || !byId[m[1]]) continue
    let node: Element | null = heading.nextElementSibling; let example: Element | null = null
    while (node && !/^H[2-4]$/.test(node.tagName)) { if (node.classList.contains('answer-example')) example = node; node = node.nextElementSibling }
    if (!example) continue
    const el = document.createElement('div'); el.className = 'team-item-slot'
    example.after(el); found.push({ sid: m[1], el })
  }
  slots.value = found; sub.value = found[0]?.sid.slice(0, 3) ?? null
  state.ready = true
})
</script>

<template>
  <section class="matrix-assessment team-assessment" aria-labelledby="team-assessment-title">
    <h2 id="team-assessment-title" class="matrix-assessment-title">{{ summary ? 'チームチェックの集計' : 'チームチェックの回答' }}<span>この端末のブラウザにだけ保存されます</span></h2>
    <p class="matrix-assessment-help">
      <template v-if="summary">このページの一覧と各小テーマのページで記録した回答と評価記述の集計です。</template>
      <template v-else>各項目の「望ましい回答例」の下で、回答（はい／はい、でも…／いいえ、でも…／いいえ）を選び、評価記述に実態、対象範囲、頻度、根拠資料を書きます。</template>
      配点は出典の<a href="https://dxcriteria.cto-a.org/db7e371398c2464792dc25d79e573ba1" target="_blank" rel="noopener">使い方</a>に従い、はい 1点、「でも…」は 0.5点、いいえ 0点、アンチパターンは逆転します。記録はサーバーに送られず、別の端末やブラウザには引き継がれません。確定した回答は<a :href="withBase('/templates/team-assessment.html')">チームの確認記録</a>へ転記してください。
    </p>
    <div v-if="state.ready" class="matrix-assessment-body">
      <div class="matrix-stats" role="group" aria-label="集計">
        <template v-if="!summary">
          <span class="stat stat-primary"><strong>{{ fmt(pageStats.points) }}<small>/{{ pageStats.total }}点</small></strong>この小テーマの得点</span>
          <span class="stat"><strong>{{ pageStats.answered }}<small>/{{ pageStats.total }}</small></strong>回答済み</span>
        </template>
        <span class="stat" :class="{ 'stat-primary': summary }"><strong>{{ fmt(allStats.points) }}<small>/{{ allStats.total }}点</small></strong>全体の得点</span>
        <span class="stat"><strong>{{ allStats.answered }}<small>/{{ allStats.total }}</small></strong>全体の回答済み</span>
      </div>
      <table v-if="summary" class="matrix-area-table team-summary-table">
        <thead><tr><th>大テーマ・小テーマ</th><th>回答済み</th><th>得点</th></tr></thead>
        <tbody>
          <template v-for="t in themes" :key="t.theme">
            <tr class="team-theme-row"><th>{{ t.theme }}</th><td>{{ t.answered }} / {{ t.total }}</td><td>{{ fmt(t.points) }} / {{ t.total }}</td></tr>
            <tr v-for="s in t.subs" :key="s.sub"><th class="team-sub-row"><a :href="withBase('/' + s.path.replace(/\.md$/, '.html'))">{{ s.sub }} {{ s.subtitle }}</a></th><td>{{ s.answered }} / {{ s.total }}</td><td>{{ fmt(s.points) }} / {{ s.total }}</td></tr>
          </template>
        </tbody>
      </table>
      <p v-else class="team-summary-link">全体の集計と小テーマ別の得点は<a :href="withBase('/checklists/')">チームチェックリスト</a>のページに表示されます。</p>
      <div class="matrix-actions">
        <span class="matrix-updated">最終更新：{{ state.updatedAt ?? 'なし' }}</span>
        <button type="button" class="matrix-button" @click="copy">{{ copied ? 'コピーしました' : (summary ? '全体をMarkdownでコピー' : 'この小テーマをMarkdownでコピー') }}</button>
        <button type="button" class="matrix-button matrix-button-danger" :disabled="(summary ? allStats : pageStats).answered === 0 && !(summary ? items : pageItems).some(i => entry(i.sid).note)" @click="clear((summary ? items : pageItems).map(i => i.sid))">{{ summary ? 'すべてクリア' : 'この小テーマをクリア' }}</button>
      </div>
      <details class="matrix-markdown"><summary>Markdownで表示</summary><pre>{{ markdown }}</pre></details>
    </div>
  </section>
  <Teleport v-for="s in slots" :key="s.sid" :to="s.el">
    <div class="team-item" :data-sid="s.sid">
      <p class="team-item-title">回答と評価記述<span v-if="byId[s.sid].antipattern">アンチパターン：望ましい状態は「いいえ」。配点が逆転します</span></p>
      <div class="team-options" role="group" :aria-label="`${s.sid} の回答`">
        <button v-for="o in OPTIONS" :key="o.v" type="button" class="team-option" :class="{ selected: entry(s.sid).answer === o.v }" :aria-pressed="entry(s.sid).answer === o.v" @click="setAnswer(s.sid, o.v)">{{ o.label }}</button>
        <span class="team-score" :class="{ 'is-set': score(s.sid) !== null }">{{ score(s.sid) === null ? '未回答' : `${fmt(score(s.sid)!)}点` }}</span>
      </div>
      <label class="team-note"><span>評価記述</span><textarea rows="3" :value="entry(s.sid).note" placeholder="実態、対象範囲、頻度、根拠資料を記載" @input="setNote(s.sid, ($event.target as HTMLTextAreaElement).value)"></textarea></label>
    </div>
  </Teleport>
</template>
