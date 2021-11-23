export default [
    {
      title: '用户名',
      dataIndex: 'username',
      key:'username',
      scopedSlots: { customRender: 'username' },
    },
    {
      title: '文章总数',
      key: 'articleTotal',
      dataIndex: 'articleTotal',
    },
    {
      title: '权限',
      dataIndex: 'level',
      key: 'level',
      scopedSlots: { customRender: 'level' },
    },
    {
      title: '操作',
      dataIndex: 'operation',
      scopedSlots: { customRender: 'operation' },
    },
];