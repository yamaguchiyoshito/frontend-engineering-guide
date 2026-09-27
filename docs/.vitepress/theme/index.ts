import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Downloads from './Downloads.vue'
import manifest from '../../public/downloads/manifest.json'
import './style.css'
export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-before': () => h('div', { class: 'document-meta' }, [
      h('span', '公開基準'), h('span', `文書版 ${manifest.version}`)
    ])
  }),
  enhanceApp({ app }) { app.component('Downloads', Downloads) }
}
