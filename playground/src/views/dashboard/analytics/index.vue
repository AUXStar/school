<script lang="ts" setup>
import type { AnalysisOverviewItem } from '@vben/common-ui';
import type { TabOption } from '@vben/types';

import {
  AnalysisChartCard,
  AnalysisChartsTabs,
  AnalysisOverview,
} from '@vben/common-ui';
import {
  SvgBell1Icon,
  SvgBellIcon,
  SvgCakeIcon,
  SvgCardIcon,
} from '@vben/icons';

// import { rTime } from '#/utils/dayjs';

import AnalyticsTrends from './analytics-trends.vue';
import AnalyticsVisits from './analytics-visits.vue';
import AnalyticsVisitsData from './analytics-visits-data.vue';
import AnalyticsVisitsSales from './analytics-visits-sales.vue';
// import AnalyticsVisitsSource from './analytics-visits-source.vue';

const overviewItems: AnalysisOverviewItem[] = [
  {
    icon: SvgCardIcon,
    title: '过去1h平均心率',
    totalTitle: '健康指数',
    totalValue: 86,
    value: 75,
  },
  {
    icon: SvgCakeIcon,
    title: '未完成任务',
    totalTitle: '总任务量',
    totalValue: 10,
    value: 3,
  },
  {
    icon: SvgBell1Icon,
    title: '今日报警触发次数',
    totalTitle: '总报警触发次数',
    totalValue: 20,
    value: 5,
  },
  {
    icon: SvgBellIcon,
    title: '资料库访问量',
    totalTitle: '全校资料库访问量',
    totalValue: 50_440,
    value: 78,
  },
];

const chartTabs: TabOption[] = [
  {
    label: '本日运动统计',
    value: 'trends',
  },
  {
    label: '月任务完成率',
    value: 'visits',
  },
];
</script>

<template>
  <div class="p-5">
    <AnalysisOverview :items="overviewItems" />
    <AnalysisChartsTabs :tabs="chartTabs" class="mt-5">
      <template #trends>
        <AnalyticsTrends />
      </template>
      <template #visits>
        <AnalyticsVisits />
      </template>
    </AnalysisChartsTabs>

    <div class="mt-5 w-full md:flex">
      <AnalysisChartCard
        class="mt-5 md:mr-4 md:mt-0 md:w-1/2"
        title="学科能力统计"
      >
        <AnalyticsVisitsData />
      </AnalysisChartCard>
      <!-- <AnalysisChartCard class="mt-5 md:mr-4 md:mt-0 md:w-1/3" title="访问来源">
        <AnalyticsVisitsSource /> -->
      <!-- </AnalysisChartCard> -->
      <AnalysisChartCard class="mt-5 md:mt-0 md:w-1/2" title="访问统计">
        <AnalyticsVisitsSales />
      </AnalysisChartCard>
    </div>
  </div>
</template>
