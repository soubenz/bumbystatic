// This is where project configuration and plugin options are located. 
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

module.exports = {
  chainWebpack: config => {
    config.resolve.alias.set('@images', '@/assets/images')
  },
  // siteName: 'TV Series Quotes',
  plugins: [{
      use: 'gridsome-plugin-service-worker',
      options: {
        networkFirst: {
          routes: [
            "/",
            /\.(js|css|png)$/, // means "every JS, CSS, and PNG images"
          ],
        },

      }
    },
    {
      use: "gridsome-plugin-manifest",
      options: {
        background_color: "#000000",
        icon_path: "./src/assets/images/logo.png",
        name: process.env.DATA_USER + "'s App",
        display: "standalone",
        short_name: process.env.DATA_USER,
        theme_color: "#FFFFFF",
        lang: "en",
        start_url: "/"
      }
    }
  ],
  templates: {
    // Influencers: '/influencer/:username',
    // Blogs: '/blog/:username',
    // Quotes: '/quotes/:id',
    Users: '/',
    // Links2: '/2/:id',
    // Links3: '/3/:id',
    // Links4: '/4/:id',
    // Links5: '/5/:id',
    // Pages: '/:name/:id'
  }

}