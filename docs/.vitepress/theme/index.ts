import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Downloads from './Downloads.vue'
import MatrixAssessment from './MatrixAssessment.vue'
import SidebarToggle from './SidebarToggle.vue'
import TeamAssessment from './TeamAssessment.vue'
import manifest from '../../public/downloads/manifest.json'
import './style.css'
export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-before': () => h('div', { class: 'document-meta' }, [
      h('span', '公開基準'), h('span', `文書版 ${manifest.version}`)
    ]),
    'sidebar-nav-before': () => h(SidebarToggle)
  }),
  enhanceApp({ app }) { app.component('Downloads', Downloads); app.component('MatrixAssessment', MatrixAssessment); app.component('TeamAssessment', TeamAssessment) }
}
