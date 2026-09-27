<script setup lang="ts">
import { withBase } from 'vitepress'
import manifest from '../../public/downloads/manifest.json'
</script>
<template>
  <p class="download-version">文書版 {{ manifest.version }} · 生成元 {{ manifest.commit.slice(0, 12) }}</p>
  <ul class="downloads-list">
    <li v-for="file in manifest.files" :key="file.name">
      <a :href="withBase('/downloads/' + file.name)" :download="file.name">
        <strong>{{ file.title }}</strong>
        <span>{{ file.description }} · {{ Math.ceil(file.bytes / 1024) }} KB</span>
      </a>
    </li>
  </ul>
  <details class="download-provenance">
    <summary>生成元とファイルの検証</summary>
    <p>生成日時（UTC）：{{ manifest.generatedAt }}<br>生成元コミット：<code>{{ manifest.commit }}</code></p>
    <p><a :href="withBase('/downloads/manifest.json')" download="manifest.json">版・コミット・SHA-256を記録したJSON</a></p>
  </details>
</template>
