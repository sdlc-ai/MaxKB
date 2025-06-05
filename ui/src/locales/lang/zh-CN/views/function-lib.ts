export default {
  title: '插件库',
  internalTitle: '内置插件',
  added: '已添加',
  createFunction: '创建插件',
  editFunction: '编辑插件',
  copyFunction: '复制插件',
  importFunction: '导入插件',
  searchBar: {
    placeholder: '按插件名称搜索',
    search:'搜索'
  },
  setting: {
    disabled: '禁用'
  },
  tip: {
    saveMessage: '当前的更改尚未保存，确认退出吗?'
  },
  delete: {
    confirmTitle: '是否删除插件：',
    confirmMessage: '删除后，引用了该插件的应用提问时会报错 ，请谨慎操作。'
  },
  disabled: {
    confirmTitle: '是否禁用插件：',
    confirmMessage: '禁用后，引用了该插件的应用提问时会报错 ，请谨慎操作。'
  },
  functionForm: {
    title: {
      copy: '副本',
      baseInfo: '基础信息'
    },
    form: {
      functionName: {
        label: '名称',
        name: '插件名称',
        placeholder: '请输入插件名称',
        requiredMessage: '请输入插件名称'
      },
      functionDescription: {
        label: '描述',
        placeholder: '请输入插件的描述'
      },
      permission_type: {
        label: '权限',
        requiredMessage: '请选择'
      },
      paramName: {
        label: '参数名',
        placeholder: '请输入参数名',
        requiredMessage: '请输入参数名'
      },
      dataType: {
        label: '数据类型'
      },
      source: {
        label: '来源',
        custom: '自定义',
        reference: '引用参数'
      },
      required: {
        label: '是否必填'
      },
      param: {
        paramInfo1: '使用插件时显示',
        paramInfo2: '使用插件时不显示',
        code: '插件内容（Python）',
        selectPlaceholder: '请选择参数',
        inputPlaceholder: '请输入参数值'
      },
      debug: {
        run: '运行',
        output: '输出',
        runResult: '运行结果',
        runSuccess: '运行成功',
        runFailed: '运行失败'
      }
    }
  }
}
