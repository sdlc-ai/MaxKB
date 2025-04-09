# MaxKB 项目结构

## 项目根目录
- main.py (主程序入口)
- pyproject.toml (项目依赖配置)
- config_example.yml (配置文件示例)
- README.md (项目说明文档)
- README_CN.md (中文项目说明文档)
- SECURITY.md (安全说明文档)
- LICENSE (许可证文件)
- USE-CASES.md (使用案例文档)
- CODE_OF_CONDUCT.md (行为准则)
- CONTRIBUTING.md (贡献指南)
- .gitignore (Git忽略配置)
- .dockerignore (Docker忽略配置)
- .typos.toml (拼写检查配置)

## 1. 前端模块 (ui/)
- 前端界面实现

## 2. 安装程序 (installer/)
- 安装相关程序

## 3. 应用模块 (apps/)

### 3.1 用户模块 (users/)
- views/
  - user.py (用户视图实现)
  - common.py (通用视图)
  - __init__.py (视图初始化)
- models/
  - user.py (用户模型定义)
  - __init__.py (模型初始化)
- serializers/
  - user_serializers.py (用户数据序列化)
- urls.py (URL路由配置)
- apps.py (应用配置)

### 3.2 智能文档模块 (smartdoc/)
- settings/
  - lib.py (库配置)
  - logging.py (日志配置)
  - auth.py (认证配置)
  - base.py (基础配置)
  - __init__.py (配置初始化)
- wsgi.py (WSGI配置)
- urls.py (URL路由)
- const.py (常量定义)
- conf.py (配置文件)
- asgi.py (ASGI配置)

### 3.3 设置模块 (setting/)
- views/
  - valid.py (验证视图)
  - model.py (模型视图)
  - model_apply.py (模型应用视图)
  - system_setting.py (系统设置视图)
  - Team.py (团队管理视图)
  - common.py (通用视图)
  - __init__.py (视图初始化)
- urls.py (URL路由)
- apps.py (应用配置)

### 3.4 运维模块 (ops/)
- celery/ (Celery任务队列)
- __init__.py (初始化文件)

### 3.5 多语言支持 (locales/)
- zh_Hant/ (繁体中文)
- zh_CN/ (简体中文)
- en_US/ (英文)

### 3.6 函数库模块 (function_lib/)
- views/
  - py_lint.py (代码检查视图)
  - function_lib_views.py (函数库视图)
  - common.py (通用视图)
  - __init__.py (视图初始化)
- urls.py (URL路由)
- apps.py (应用配置)

### 3.7 嵌入模块 (embedding/)
- vector/
  - pg_vector.py (PostgreSQL向量实现)
  - base_vector.py (基础向量实现)
- views.py (视图实现)
- apps.py (应用配置)

### 3.8 数据集模块 (dataset/)
- views/
  - problem.py (问题处理视图)
  - file.py (文件处理视图)
  - image.py (图像处理视图)
  - paragraph.py (段落处理视图)
  - dataset.py (数据集处理视图)
  - document.py (文档处理视图)
  - common.py (通用视图)
  - __init__.py (视图初始化)
- urls.py (URL路由)
- apps.py (应用配置)

### 3.9 应用核心模块 (application/)
- views/
  - chat_views.py (聊天视图)
  - application_version_views.py (应用版本视图)
  - application_views.py (应用视图)
  - common.py (通用视图)
  - __init__.py (视图初始化)
- models/
  - api_key_model.py (API密钥模型)
  - application.py (应用模型)
  - __init__.py (模型初始化)
- flow/
  - workflow_manage.py (工作流管理)
  - tools.py (工具函数)
  - step_node/ (步骤节点)
  - i_step_node.py (步骤节点接口)
  - default_workflow*.json (默认工作流配置)
  - common.py (通用功能)
  - __init__.py (初始化)
- chat_pipeline/
  - step/ (步骤实现)
  - pipeline_manage.py (管道管理)
  - I_base_chat_pipeline.py (基础聊天管道接口)
  - __init__.py (初始化)
- urls.py (URL路由)
- apps.py (应用配置)

### 3.10 公共组件 (common/)
- util/ (工具类)
- template/ (模板系统)
- task/ (任务管理)
- swagger_api/ (API文档)
- sql/ (数据库操作)
- response/ (响应处理)
- models/ (数据模型)
- middleware/ (中间件)
- log/ (日志系统)
- cache/ (缓存系统)
- auth/ (认证授权)
- exception/ (异常处理)
- event/ (事件系统)
- db/ (数据库配置)

## 4. GitHub配置 (.github/)
- GitHub相关配置文件
