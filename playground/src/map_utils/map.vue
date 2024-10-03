<script setup>
import { computed, onMounted, onUnmounted, watch } from 'vue';

import { preferences, usePreferences } from '@vben/preferences';

import { amap_load } from './index';

let map = null;

const isDark = computed(() => {
  return usePreferences().isDark.value || preferences.theme.semiDarkSidebar;
});

onMounted(async () => {
  const AMap = await amap_load();
  map = new AMap.Map('map-container', {
    center: [116.397_428, 39.909_23],
    mapStyle: isDark.value ? 'amap://styles/grey' : 'amap://styles/normal',
    pitch: 50,
    showIndoorMap: true,
    viewMode: '3D',
    zoom: 11,
  });
  map.plugin(['AMap.ControlBar'], () => {
    const controlBar = new AMap.ControlBar({
      position: {
        right: '10px',
        top: '10px',
      },
    });
    map.addControl(controlBar);
  });
  map.plugin(['AMap.ToolBar'], () => {
    const controlBar = new AMap.ToolBar({
      position: {
        bottom: '100px',
        right: '10px',
      },
    });
    map.addControl(controlBar);
  });
  map.plugin(['AMap.Scale'], () => {
    const controlBar = new AMap.Scale({
      position: {
        bottom: '50px',
        left: '10px',
      },
    });
    map.addControl(controlBar);
  });
});

watch(isDark, (newValue, _) => {
  map.setMapStyle(newValue ? 'amap://styles/grey' : 'amap://styles/normal');
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
