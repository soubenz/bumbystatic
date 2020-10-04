// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`
// import ax from "src/ax";
// const path = require('path');
const axios = require('axios')
// module.exports = function (api) {
//   api.loadSource(({
//     addCollection
//   }) => {
//     // Use the Data Store API here: https://gridsome.org/docs/data-store-api/
//   })
const path = require('path');
module.exports = function (api) {

  api.loadSource(async actions => {

    let query = `query findAllUser {
      allUsers {
      data {_id
        username
        announcement
        companyName
        companyWebsite
        boardCaption
    }  
      
      }
    }
     `
    const {
      data
    } = await axios.post("https://graphql.fauna.com/graphql", {
      query: query
    }, {
      headers: {
        Authorization: "Basic Zm5BRHRxUnA1MkFDRTBrMzlmWkVTMnR4bXNHZ2JScEVVUGRvZ1d4WjpidW1ieTpzZXJ2ZXI="
      }
    })


    console.log(data)
    const layouts = actions.addCollection('User')
    // layouts.addReference('layouts', 'Layout')
    data.data.allUsers.data.forEach(user => {
      layouts.addNode({
        id: user.username,
        companyName: user.companyName,
        companyWebsite: user.companyWebsite,
        announcement: user.announcement,
        boardCaption: user.boardCaption
        // id: quote.image.slice(-25, -5),
        //  image: path.resolve(quote.image),
        //  id: quote.text.slice(0, 30),
        //  character: quote.character,
        //  series: actions.store.createReference(tvseries),
        //  text: quote.text

      })
    })
  })
}

// });

// for (let item of data) {
//   const coll = actions.getCollection(item.theme)
//   // const t = layout.addNode(item.layout)
//   // var k
//   // for (let block of item.layout) {
//   //   k = layouts.addNode(block)
//   // }
//   const p = coll.addNode({
//     id: item.user_id,
//     bio: item.bio,
//     name: item.name,
//     profileImg: item.profile_img,
//     // items: item.items,
//     layout: item.layout,
//     // layout: [k],
//     theme: item.theme,
//     style: item.style,
//     header: item.header,
//     animation: item.animation
//     // quotes: item.quotes,
//     // genre: item.genre,
//     // year: item.year
//     // quotes: actions.store.createReference(allQuotes)

//   })
// item.quotes.forEach(quote => {
//   quotes.addNode({
//     // id: quote.image.slice(-25, -5),
//     image: path.resolve(quote.image),
//     id: quote.text.slice(0, 30),
//     character: quote.character,
//     series: actions.store.createReference(tvseries),
//     text: quote.text
//   })

// });



// }
// }
// api.createPages(async ({
//   graphql,
//   createPage
// }) => {
//   const {
//     data
//   } = await graphql(`{
//     allKitInfluencers {
//       edges {
//         node {
//           id
//           title
//         }
//       }
//     }
//   }`)

//   data.allKitInfluencers.edges.forEach(({
//     node
//   }) => {
//     createPage({
//       path: `/test/${node.title}`,
//       component: './src/templates/KitInfluencers.vue',
//       context: {
//         id: node.id
//       }
//     })
//   })
// })

// api.createPages(({
//   createPage
// }) => {
//   createPage({
//     path: '/my-page',
//     component: './src/templates/KitInfluencer.vue'
//   })
//   // Use the Pages API here: https://gridsome.org/docs/pages-api/
// })
// }