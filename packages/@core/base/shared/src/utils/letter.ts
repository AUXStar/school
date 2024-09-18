/**
 * 将字符串的首字母大写
 * @param string
 */
const capitalizeFirstLetter = (str: string): string => 
  str ? `${str.charAt(0).toUpperCase()}${str.slice(1)}` : str;

/**
 * 将字符串的首字母转换为小写。
 *
 * @param str 要转换的字符串
 * @returns 首字母小写的字符串
 */
const toLowerCaseFirstLetter = (str: string): string => 
  str ? `${str.charAt(0).toLowerCase()}${str.slice(1)}` : str;

/**
 *  生成驼峰命名法的键名
 * @param key
 * @param parentKey
 */
const toCamelCase = (key: string, parentKey: string): string => 
  parentKey ? `${parentKey}${capitalizeFirstLetter(key)}` : key;

function kebabToCamelCase(str: string): string {
  return str
    .split('-')
    .filter(Boolean)
    .map((word, index) => index === 0 ? word : capitalizeFirstLetter(word))
    .join('');
}

export { capitalizeFirstLetter, toLowerCaseFirstLetter, toCamelCase, kebabToCamelCase };
