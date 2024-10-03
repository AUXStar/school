<script lang="ts" setup>
import { onMounted, onUnmounted } from 'vue';

import AMapLoader from '@amap/amap-jsapi-loader';

let map: { destroy: () => void } | null = null;

onMounted(() => {
  window._AMapSecurityConfig = {
    securityJsCode: 'b0ffe70823c342414ef1207583b3b377',
  };
  AMapLoader.load({
    key: '69c705c6a8e9722ea36fa4887d07b26b', // 申请好的Web端开发者Key，首次调用 load 时必填
    plugins: ['AMap.Scale'], // 需要使用的的插件列表，如比例尺'AMap.Scale'，支持添加多个如：['...','...']
    version: '2.0', // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
  })
    .then((AMap) => {
      map = new AMap.Map('map-container', {
        center: [116.397_428, 39.909_23], // 初始化地图中心点位置
        // 设置地图容器id
        viewMode: '3D', // 是否为3D地图模式
        zoom: 11, // 初始化地图级别
      });
    })
    .catch((error) => {
      // eslint-disable-next-line no-console
      console.log(error);
    });
});

onUnmounted(() => {
  map?.destroy();
});
</script>

<template>
  <div id="map-container"></div>
</template>

<style scoped>
#map-container {
  width: 100%;
  height: 800px;
}
</style>
