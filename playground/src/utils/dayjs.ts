import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';

// 加载中文语言包
import 'dayjs/locale/zh-cn';

// 配置使用处理相对时间的插件
dayjs.extend(relativeTime);

// 配置使用中文语言包
dayjs.locale('zh-cn');

function rTime(value: any) {
  return dayjs().to(dayjs(value));
}

export { rTime };
