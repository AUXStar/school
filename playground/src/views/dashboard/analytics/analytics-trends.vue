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
    grid: {
      bottom: 0,
      containLabel: true,
      left: '1%',
      right: '1%',
      top: '2 %',
    },
    series: [
      {
        areaStyle: {},
        data: [
          11, 200, 600, 1600, 3333, 5555, 6400, 3333, 1800, 3600, 7000, 400,
          100, 4244, 2322, 1300, 800, 33, 22, 111,
        ],
        itemStyle: {
          color: '#5ab1ef',
        },
        smooth: false,
        type: 'line',
      },
      {
        areaStyle: {},
        data: [
          33, 66, 88, 333, 3333, 6200, 20_000, 3000, 1200, 1300, 2200, 1100,
          2221, 1201, 390, 198, 60, 30, 22, 11,
        ],
        itemStyle: {
          color: '#019680',
        },
        smooth: false,
        type: 'line',
      },
    ],
    tooltip: {
      axisPointer: {
        lineStyle: {
          color: '#019680',
          width: 1,
        },
      },
      trigger: 'axis',
    },
    // xAxis: {
    //   axisTick: {
    //     show: false,
    //   },
    //   boundaryGap: false,
    //   data: Array.from({ length: 18 }).map((_item, index) => `${index + 6}:00`),
    //   type: 'category',
    // },
    xAxis: {
      axisTick: {
        show: false,
      },
      boundaryGap: false,
      data: Array.from({ length: 18 }).map((_item, index) => `${index + 6}:00`),
      splitLine: {
        lineStyle: {
          type: 'solid',
          width: 1,
        },
        show: true,
      },
      type: 'category',
    },
    yAxis: [
      {
        axisTick: {
          show: false,
        },
        max: 20_000,
        splitArea: {
          show: true,
        },
        splitNumber: 5,
        type: 'value',
      },
    ],
  });
});
</script>

<template>
  <EchartsUI ref="chartRef" />
</template>
