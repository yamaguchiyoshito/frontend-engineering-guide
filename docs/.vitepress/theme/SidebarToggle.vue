<script setup lang="ts">
import { ref, onMounted } from 'vue'

/** Full / compact sidebar. The choice is kept in localStorage and applied before paint by a head script in config.ts. */
const KEY = 'fe-guide.sidebar'
const compact = ref(false)
function apply() {
  document.documentElement.dataset.sidebar = compact.value ? 'compact' : 'full'
  try { localStorage.setItem(KEY, compact.value ? 'compact' : 'full') } catch { /* ignore */ }
}
function toggle() { compact.value = !compact.value; apply() }
onMounted(() => { compact.value = document.documentElement.dataset.sidebar === 'compact' })
</script>

<template>
  <button type="button" class="sidebar-toggle" :class="{ compact }" :aria-pressed="compact" :aria-label="compact ? '目次を表示' : '目次をコンパクト表示'" :title="compact ? '目次を表示' : '目次をコンパクト表示'" @click="toggle">
    <span class="sidebar-toggle-icon" aria-hidden="true">{{ compact ? '»' : '«' }}</span><span class="sidebar-toggle-text">目次をコンパクト表示</span>
  </button>
</template>
