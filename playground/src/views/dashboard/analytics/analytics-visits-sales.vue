<script lang="ts" setup>
import { onMounted, ref } from 'vue';

import {
  EchartsUI,
  type EchartsUIType,
  useEcharts,
} from '@vben/plugins/echarts';

const chartRef = ref<EchartsUIType>();
const { renderEcharts } = useEcharts(chartRef);

onMounted(() => {
  renderEcharts({
    series: [
      {
        animationDelay() {
          return Math.random() * 400;
        },
        animationEasing: 'exponentialInOut',
        animationType: 'scale',
        center: ['50%', '50%'],
        color: ['#5ab1ef', '#b6a2de', '#67e0e3', '#2ec7c9'],
        data: [
          { name: '数学', value: 50 },
          { name: '语文', value: 710 },
          { name: '英语', value: 274 },
          { name: '化学', value: 400 },
          { name: '物理', value: 100 },
          { name: '政治', value: 120 },
          { name: '历史', value: 300 },
          { name: '生物', value: 200 },
          { name: '地理', value: 500 },
        ].sort((a, b) => {
          return a.value - b.value;
        }),
        name: '访问占比',
        radius: '80%',
        roseType: 'radius',
        type: 'pie',
      },
    ],

    tooltip: {
      trigger: 'item',
    },
  });
});
</script>

<template>
  <EchartsUI ref="chartRef" />
</template>
