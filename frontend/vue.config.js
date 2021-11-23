const path = require('path')

function resolve(dir) { 
  return path.join(__dirname, dir)
}
module.exports = {  
    publicPath:'./',
    lintOnSave:true,
    devServer: {
        open:true
    },
    // webpack 打包顺序
    chainWebpack:(config)=>{
        config.resolve.alias
            .set('@',resolve('src/components'))
            .set('~', resolve('src'))
    },
    // eslint-disable-next-line no-dupe-keys
    devServer: {
      proxy:{
        '/api': {
          target: 'http://127.0.0.1:3000/',
          ws: true,
          changeOrigin: true,
          pathRewrite: {
            '^/api':''
          }
        }
      }
    },
    pages: {
      index: {
        // page 的入口
        entry: 'src/pages/index/main.js',
        // 模板来源
        template: 'public/index.html',
        // 在 dist/index.html 的输出
        filename: 'index.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: 'tree hole',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'index']
      },
      admin: {
        entry: 'src/pages/admin/main.js',
        template: 'public/index.html',
        filename: 'admin.html',
        title: '博客管理后台',
        chunks: ['chunk-vendors', 'chunk-common', 'admin']
      },
    }
}