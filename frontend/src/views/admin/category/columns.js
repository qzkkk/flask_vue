export default [
    {
      title: '分类名称',
      dataIndex: 'title',
      key:'title',
      scopedSlots: { customRender: 'title' },
    },
    {
      title: '分类描述',
      dataIndex: 'description',
    },
    {
      title: '操作',
      dataIndex: 'operation',
      scopedSlots: { customRender: 'operation' },
    },
];