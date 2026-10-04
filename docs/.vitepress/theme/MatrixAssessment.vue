<script setup lang="ts">
import { onMounted, onBeforeUnmount, reactive, computed, ref } from 'vue'
import { withBase } from 'vitepress'

/** Self-assessment on the skill matrix: one Lv per skill, kept in this browser's localStorage only. */
const KEY = 'fe-guide.assessment.v1'
const LEVELS = ['Lv0', 'Lv1', 'Lv2', 'Lv3', 'Lv4']
type Row = { id: string; title: string; area: string; cells: HTMLTableCellElement[]; marker: HTMLElement }
const rows: Row[] = []
const areas: string[] = []
const state = reactive<{ levels: Record<string, number>; updatedAt: string | null; ready: boolean }>({ levels: {}, updatedAt: null, ready: false })
const copied = ref(false)
const cleanups: (() => void)[] = []

function load() {
  try {
    const raw = localStorage.getItem(KEY)
    if (!raw) return
    const data = JSON.parse(raw)
    if (data && typeof data === 'object' && data.levels) {
      for (const [id, lv] of Object.entries(data.levels)) if (Number.isInteger(lv) && (lv as number) >= 0 && (lv as number) <= 4) state.levels[id] = lv as number
      state.updatedAt = typeof data.updatedAt === 'string' ? data.updatedAt : null
    }
  } catch { /* private mode or blocked storage: the page still works, nothing persists */ }
}
function save() {
  try { localStorage.setItem(KEY, JSON.stringify({ version: 1, updatedAt: state.updatedAt, levels: state.levels })) } catch { /* ignore */ }
}
function paint(row: Row) {
  const lv = state.levels[row.id]
  row.cells.forEach((td, i) => {
    td.classList.toggle('is-selected', lv === i)
    td.classList.toggle('is-passed', lv !== undefined && i < lv)
    td.setAttribute('aria-pressed', lv === i ? 'true' : 'false')
  })
  row.marker.textContent = lv === undefined ? '未評価' : LEVELS[lv]
  row.marker.classList.toggle('is-set', lv !== undefined)
}
function set(row: Row, lv: number) {
  if (state.levels[row.id] === lv) delete state.levels[row.id]; else state.levels[row.id] = lv
  state.updatedAt = new Date().toISOString().slice(0, 10)
  save(); paint(row)
}
function clearAll() {
  if (!confirm('この端末に保存した自己評価をすべて消します。よろしいですか？')) return
  for (const id of Object.keys(state.levels)) delete state.levels[id]
  state.updatedAt = null
  try { localStorage.removeItem(KEY) } catch { /* ignore */ }
  rows.forEach(paint)
}

onMounted(() => {
  load()
  const table = document.querySelector<HTMLTableElement>('.skill-matrix table')
  if (!table) return
  let area = ''
  for (const tr of Array.from(table.tBodies[0]?.rows ?? [])) {
    const first = tr.cells[0]
    const areaLabel = first.querySelector('.matrix-area')
    if (areaLabel) { area = areaLabel.textContent?.trim() ?? ''; if (!areas.includes(area)) areas.push(area); continue }
    const id = first.querySelector('code')?.textContent?.trim()
    const title = first.querySelector('a')?.textContent?.trim()
    if (!id || !title) continue
    const marker = document.createElement('span')
    marker.className = 'row-level'
    first.appendChild(marker)
    const cells = Array.from(tr.cells).slice(1, 6) as HTMLTableCellElement[]
    const row: Row = { id, title, area, cells, marker }
    cells.forEach((td, i) => {
      td.classList.add('lv-cell')
      td.setAttribute('role', 'button'); td.setAttribute('tabindex', '0')
      td.setAttribute('aria-label', `${title} を ${LEVELS[i]} として記録`)
      const mark = document.createElement('span'); mark.className = 'lv-mark'; mark.textContent = '選択中'
      td.prepend(mark)
      const onClick = (e: Event) => { if ((e.target as HTMLElement).closest('a')) return; set(row, i) }
      const onKey = (e: KeyboardEvent) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(row, i) } }
      td.addEventListener('click', onClick); td.addEventListener('keydown', onKey)
      cleanups.push(() => { td.removeEventListener('click', onClick); td.removeEventListener('keydown', onKey) })
    })
    rows.push(row); paint(row)
  }
  state.ready = true
})
onBeforeUnmount(() => cleanups.forEach(f => f()))

const total = computed(() => rows.length)
const assessed = computed(() => rows.filter(r => state.levels[r.id] !== undefined).length)
const byLevel = computed(() => LEVELS.map((_, lv) => rows.filter(r => state.levels[r.id] === lv).length))
const byArea = computed(() => areas.map(a => {
  const list = rows.filter(r => r.area === a)
  return { area: a, total: list.length, assessed: list.filter(r => state.levels[r.id] !== undefined).length, levels: LEVELS.map((_, lv) => list.filter(r => state.levels[r.id] === lv).length) }
}))
const markdown = computed(() => {
  const lines = [`# 習熟度マトリクスの自己評価（${state.updatedAt ?? '未記録'}）`, '', `評価済み ${assessed.value} / ${total.value}（未評価 ${total.value - assessed.value}）`]
  for (const a of areas) {
    lines.push('', `## ${a}`, '')
    for (const r of rows.filter(r => r.area === a)) lines.push(`- ${r.title}（\`${r.id}\`）：${state.levels[r.id] === undefined ? '未評価' : LEVELS[state.levels[r.id]]}`)
  }
  return lines.join('\n') + '\n'
})
async function copy() {
  try { await navigator.clipboard.writeText(markdown.value); copied.value = true; setTimeout(() => (copied.value = false), 2000) } catch { copied.value = false }
}
</script>

<template>
  <section class="matrix-assessment" aria-labelledby="matrix-assessment-title">
    <h2 id="matrix-assessment-title" class="matrix-assessment-title">自己評価の記録<span>この端末のブラウザにだけ保存されます</span></h2>
    <p class="matrix-assessment-help">表のLv0〜Lv4のセルを選ぶと、その要素技術の自己評価として記録されます。同じセルをもう一度選ぶと未評価に戻ります。記録はサーバーに送られず、別の端末やブラウザには引き継がれません。確定した評価は<a :href="withBase('/templates/individual-assessment.html')">個人の習熟度評価記録</a>へ転記してください。</p>
    <div v-if="state.ready" class="matrix-assessment-body">
      <div class="matrix-stats" role="group" aria-label="集計">
        <span class="stat stat-primary"><strong>{{ assessed }}<small>/{{ total }}</small></strong>評価済み</span>
        <span class="stat"><strong>{{ total - assessed }}</strong>未評価</span>
        <span v-for="(n, lv) in byLevel" :key="lv" class="stat"><strong>{{ n }}</strong>{{ LEVELS[lv] }}</span>
      </div>
      <table class="matrix-area-table">
        <thead><tr><th>領域</th><th>評価済み</th><th v-for="l in LEVELS" :key="l">{{ l }}</th><th>未評価</th></tr></thead>
        <tbody>
          <tr v-for="a in byArea" :key="a.area"><th>{{ a.area }}</th><td>{{ a.assessed }} / {{ a.total }}</td><td v-for="(n, i) in a.levels" :key="i">{{ n || '' }}</td><td>{{ a.total - a.assessed || '' }}</td></tr>
        </tbody>
      </table>
      <div class="matrix-actions">
        <span class="matrix-updated">最終更新：{{ state.updatedAt ?? 'なし' }}</span>
        <button type="button" class="matrix-button" @click="copy">{{ copied ? 'コピーしました' : 'Markdownでコピー' }}</button>
        <button type="button" class="matrix-button matrix-button-danger" :disabled="assessed === 0" @click="clearAll">すべてクリア</button>
      </div>
      <details class="matrix-markdown"><summary>Markdownで表示</summary><pre>{{ markdown }}</pre></details>
    </div>
  </section>
</template>
