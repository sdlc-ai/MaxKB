import Layout from '@/layout/layout-template/DetailLayout.vue'
import { ComplexPermission } from '@/utils/permission/type'

const applicationRouter = {
  path: '/application',
  name: 'application',
  meta: { title: 'views.application.title', permission: 'APPLICATION:READ' },
  redirect: '/application',
  component: () => import('@/layout/layout-template/AppLayout.vue'),
  children: [
    {
      path: '/application',
      name: 'application-index',
      meta: { title: '应用主页', activeMenu: '/application' },
      component: () => import('@/views/application/index.vue')
    },
    {
      path: '/application/:id/:type',
      name: 'ApplicationDetail',
      meta: { title: '应用详情', activeMenu: '/application' },
      component: Layout,
      hidden: true,
      children: [
        {
          path: 'overview',
          name: 'AppOverview',
          meta: {
            icon: 'ri-pie-chart-2-line',
            iconActive: 'ri-pie-chart-2-fill',
            title: 'views.applicationOverview.title',
            active: 'overview',
            parentPath: '/application/:id/:type',
            parentName: 'ApplicationDetail'
          },
          component: () => import('@/views/application-overview/index.vue')
        },
        {
          path: 'setting',
          name: 'AppSetting',
          meta: {
            icon: 'ri-settings-4-line',
            iconActive: 'ri-settings-4-fill',
            title: 'common.setting',
            active: 'setting',
            parentPath: '/application/:id/:type',
            parentName: 'ApplicationDetail'
          },
          component: () => import('@/views/application/ApplicationSetting.vue')
        },
        {
          path: 'access',
          name: 'AppAccess',
          meta: {
            icon: 'app-access',
            iconActive: 'app-access-active',
            title: 'views.application.applicationAccess.title',
            active: 'access',
            parentPath: '/application/:id/:type',
            parentName: 'ApplicationDetail',
            permission: new ComplexPermission([], ['x-pack'], 'OR')
          },
          component: () => import('@/views/application/ApplicationAccess.vue')
        },
        {
          path: 'hit-test',
          name: 'AppHitTest',
          meta: {
            icon: 'ri-focus-2-line',
            iconActive: 'ri-focus-2-fill',
            title: 'views.application.hitTest.title',
            active: 'hit-test',
            parentPath: '/application/:id/:type',
            parentName: 'ApplicationDetail'
          },
          component: () => import('@/views/hit-test/index.vue')
        },
        {
          path: 'log',
          name: 'Log',
          meta: {
            icon: 'ri-message-2-line',
            iconActive: 'ri-message-2-fill',
            title: 'views.log.title',
            active: 'log',
            parentPath: '/application/:id/:type',
            parentName: 'ApplicationDetail'
          },
          component: () => import('@/views/log/index.vue')
        }
      ]
    }
  ]
}

export default applicationRouter
