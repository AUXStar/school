import type { RouteRecordRaw } from 'vue-router';

import { BasicLayout } from '#/layouts';
import { $t } from '#/locales';

const routes: RouteRecordRaw[] = [
  {
    component: BasicLayout,
    meta: {
      icon: 'mdi:account-box-multiple-outline',
      order: 200,
      title: $t('page.other.title'),
    },
    name: 'Other',
    path: '/other',
    children: [
      {
        component: () => import('#/views/_core/other/about.vue'),
        name: 'About',
        path: '/other/about',
        meta: {
          icon: 'mdi:account-box-multiple-outline',
          order: 100,
          title: $t('page.other.about'),
        },
      },
      {
        component: () => import('#/views/_core/other/leave.vue'),
        name: 'AboutLeave',
        path: '/other/leave',
        meta: {
          icon: 'mdi:account-box-multiple-outline',
          order: 100,
          title: $t('page.other.leave'),
        },
      },
    ],
  },
];

export default routes;
