"use strict";
import Vue from 'vue'

// md 编译器
import mavonEditor from 'mavon-editor';
import 'mavon-editor/dist/css/index.css';
import "github-markdown-css";
import {
    Button,
    Input,
    Icon,
    Layout,
    Breadcrumb,
    Menu,
    Form,
    Checkbox,
    Dropdown,
    Card,
    Row,
    Col,
    Table,
    Popconfirm,
    message,
    Divider,
    Select,
    Tooltip,
    Space,
    Avatar,
    Popover,
    List,
    Timeline,
    Tag,
    Drawer,
    Calendar,
    Spin,
    Modal,
    Progress
} from 'ant-design-vue';

Vue.prototype.$message = message
Vue.use(mavonEditor)

Vue.use(Button)
    .use(Input)
    .use(Layout)
    .use(Breadcrumb)
    .use(Menu)
    .use(Form)
    .use(Checkbox)
    .use(Icon)
    .use(Dropdown)
    .use(Card)
    .use(Row)
    .use(Col)
    .use(Table)
    .use(Popconfirm)
    .use(Divider)
    .use(Select)
    .use(Tooltip)
    .use(Space)
    .use(Avatar)
    .use(Popover)
    .use(List)
    .use(Timeline)
    .use(Tag)
    .use(Drawer)
    .use(Calendar)
    .use(Spin)
    .use(Space)
    .use(Modal)
    .use(Progress)
;
