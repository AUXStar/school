interface AuthenticationProps {
  /**
   * @zh_CN 验证码登录路径
   */
  codeLoginPath?: string;
  /**
   * @zh_CN 忘记密码路径
   */
  forgetPasswordPath?: string;

  /**
   * @zh_CN 是否处于加载处理状态
   */
  loading?: boolean;

  /**
   * @zh_CN 二维码登录路径
   */
  qrCodeLoginPath?: string;

  /**
   * @zh_CN 注册路径
   */
  registerPath?: string;

  /**
   * @zh_CN 是否显示验证码登录
   */
  showCodeLogin?: boolean;
  /**
   * @zh_CN 是否显示忘记密码
   */
  showForgetPassword?: boolean;

  /**
   * @zh_CN 是否显示二维码登录
   */
  showQrcodeLogin?: boolean;

  /**
   * @zh_CN 是否显示注册按钮
   */
  showRegister?: boolean;

  /**
   * @zh_CN 是否显示记住账号
   */
  showRememberMe?: boolean;

  /**
   * @zh_CN 是否显示第三方登录
   */
  showThirdPartyLogin?: boolean;

  /**
   * @zh_CN 登录框子标题
   */
  subTitle?: string;

  /**
   * @zh_CN 登录框标题
   */
  title?: string;
}

interface LoginParams {
  password: string;
  username: string;
}
interface RegisterParams {
  password: string;
  username: string;
  id_card: string;
  phone: string;
  realname: string;
  is_male: boolean | string;
}

interface LoginCodeParams {
  code: string;
  phoneNumber: string;
}

interface LoginEmits {
  submit: [LoginParams];
}

interface LoginCodeEmits {
  submit: [LoginCodeParams];
}

interface RegisterEmits {
  submit: [RegisterParams];
}

export type {
  AuthenticationProps,
  LoginCodeEmits,
  LoginCodeParams,
  LoginEmits,
  LoginParams,
  RegisterEmits,
  RegisterParams,
};
