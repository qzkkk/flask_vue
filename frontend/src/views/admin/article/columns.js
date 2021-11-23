export default [
    {
      title: "id",
      dataIndex: "id"
    },
    {
      title: "作者",
      dataIndex: "author",
    },
    {
      title: "文章体",
      dataIndex: "body",
    },
    {
      title: "操作",
      dataIndex: "operation",
      scopedSlots: { customRender: "operation" },
    },
];