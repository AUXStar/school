import AMapLoader from '@amap/amap-jsapi-loader';

let amap_cache = null;

export async function amap_load(useCache = true) {
  if (amap_cache && useCache) {
    return amap_cache;
  }
  window._AMapSecurityConfig = {
    securityJsCode: 'b0ffe70823c342414ef1207583b3b377',
  };

  const loader = await AMapLoader.load({
    key: '69c705c6a8e9722ea36fa4887d07b26b', // 必填
    plugins: ['AMap.Scale', 'AMap.ToolBar', 'AMap.ControlBar'],
    version: '2.0',
  });
  amap_cache = loader;
  return loader;
}
