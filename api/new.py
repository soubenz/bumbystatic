import json
from itertools import groupby
import hashlib
from faker import Faker

f = Faker()


def mock_links():

    data = [{
        "user_id":
        f.random_int(min=20, max=1000, step=1),
        "name":
        f.name(),
        "bio":
        f.paragraph(nb_sentences=5,
                    variable_nb_sentences=True,
                    ext_word_list=None),
        "style": ["dd", 'ddfg'],
        "header": "Animation",
        "animation": f.random_element(elements=('welcome_1', 'welcome_2', 'welcome_3', 'welcome_5')),
        "theme": f.random_element(elements=('Links1', 'Links2', 'Links3', 'Links4', 'Links5')),
        # "theme":'Links1',
        "profile_img": "http://cleanfooddirtycity.com/wp-content/uploads/2015/11/Clean-Food-Dirty-City-4-212x300.jpg",
        "layout": [{"links": [{
            "type": f"link",
            "id": f.pyint(min_value=0, max_value=9999, step=1),
            "text": f"test_{n}",
            "href": f.uri(),
            "is_activated": f.pybool()
        }
            for x in range(1, f.pyint(min_value=2, max_value=5, step=1))
        ]}, {"text": {"content":  f.paragraph(nb_sentences=1),  "size": "2"}},
            {"text": {"content":  f.paragraph(nb_sentences=2),  "size": "5"}}]

    } for n in range(20)]
    print(data)
    return data


def mock_layout():

    data = {
        "user_id":
        f.random_int(min=20, max=1000, step=1),
        "name":
        f.name(),
        "bio":
        f.paragraph(nb_sentences=5,
                    variable_nb_sentences=True,
                    ext_word_list=None),
        "layout": [{
            "id": f.hexify(text='^^^^', upper=False),
            "color": "#1F7087",
            "title": "Supermodel",
            "name": "Image",
            "type": "ImageBlock",
            "aspectRatio": "-1.7",
            "imageIcon": "image",
        }, {
            "id": f.hexify(text='^^^^', upper=False),
            "buttonColor": "#00FF00",
            "buttonTextcolor": "black",
            "buttonSize": "classic",
            "buttonStyle": "rounded",
            "isRipple": True,
            "name": "Links",
            "type": "ButtonBlock",
            "buttonText": "Promotion",
            "buttonLink": "#",
        }, {
            "id": f.hexify(text='^^^^', upper=False),
            "color": "#952175",
            "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
            "title": "fHalcweyon Daysf",
            "name": "Text",
            "type": "TextBlock",
            "textTitle": "headline",
            "textDescription": "this is a desc",
            "imageIcon": "mdi-format-text",
        }, {
            "id": f.hexify(text='^^^^', upper=False),
            "color": "#1F7087",
            "src": "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
            "title": "Supermffwodel",
            "name": "Avatar",
            "type": "AvatarBlock",
            "thumbnail": "",
            "imageIcon": "mdi-face-recognition",
        }, {
            "id": f.hexify(text='^^^^', upper=False),
            "color": "#1F7087",
            "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
            "title": "Halcdfdfyon Days",
            "name": "Optin",
            "type": "OptinBlock",
            "block": True,
            "thumbnail": "",
            "imageIcon": "mdi-email-edit-outline",
        }, {
            "id": f.hexify(text='^^^^', upper=False),
            "color": "#1F7087",
            "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
            "name": "Divider",
            "type": "DividerBlock",
        }, {
            "id": f.hexify(text='^^^^', upper=False),
            "buttonColor": "#1F7087",
            "buttonTextcolor": "#1F7087",
            "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
            "name": "Gallery",
            "type": "GalleryBlock",
            "social": "instagram",
            "block": True,
            "thumbnail": "",
            "account": "default button",
            "buttonText": "default button",
            "imageIcon": "mdi-link-variant",
        }]
    }

    return data


def mock_community():

    data = {
        "user_id":
        "community",
        "name":
        "community",
        "bio":
        f.paragraph(nb_sentences=5,
                    variable_nb_sentences=True,
                    ext_word_list=None),
        "layout": [
            {
                "id": f.hexify(text='^^^^', upper=False),
                "color": "#1F7087",
                "title": "Supermodel",
                "name": "Image",
                "type": "ImageBlock",
                "aspectRatio": "-1.7",
                "imageIcon": "image",
            },
            {
                "id": f.hexify(text='^^^^', upper=False),
                "name": "Text",
                "type": "TextBlock",
                "textTitle": "Join Us",
                "textDescription": "By joining us, you can contribute to our rights movements and help drive transformative change for human rights, gender justice and environmental sustainability worldwide.",
                "imageIcon": "mdi-format-text",
                "descAlign": "center",
                "titleAlign": "center",
                "descFormat": "",
                "titleFormat": "bold",
                "titleColor": "",
                "descColor": "",
                "galleryImages": {"src": "", "alt": ""}
            },
            {
                "id": f.hexify(text='^^^^', upper=False),
                "buttonColor": "teal",
                "buttonTextcolor": "white",
                "buttonSize": "classic",
                "buttonStyle": "rounded",
                "isRipple": True,
                "name": "Links",
                "type": "ButtonBlock",
                "buttonText": "Donate to US",
                "buttonLink": "#",
            },
            {
                "id": f.hexify(text='^^^^', upper=False),
                "buttonColor": "teal",
                "buttonTextcolor": "white",
                "buttonSize": "classic",
                "buttonStyle": "classic",
                "isRipple": True,
                "name": "Links",
                "type": "SocialBlock",
                "social": "twitter",
                "account": "#",
            },
            {
                "id": f.hexify(text='^^^^', upper=False),
                "color": "#1F7087",
                "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
                "name": "Divider",
                "type": "DividerBlock",
            },
            {
                "id": f.hexify(text='^^^^', upper=False),
                "name": "Text",
                "type": "TextBlock",
                "textTitle": "Get community news",
                "textDescription": "Stay connected! Receive a regular selection of resources and ways to get involved with the movements.",
                "imageIcon": "mdi-format-text",
                "descAlign": "center",
                "titleAlign": "center",
                "descFormat": "",
                "titleFormat": "",
                "titleColor": "",
                "descColor": "",
            },



            {
                "id": f.hexify(text='^^^^', upper=False),
                "buttonColor": "teal",
                "buttonTextcolor": "white",
                "buttonSize": "classic",
                "buttonStyle": "rounded",
                "isRipple": True,
                "name": "Links",
                "type": "OptinBlock",
                "optinText": "Signup! ",
                "buttonLink": "#",
            },

            # {
            #     "id": f.hexify(text='^^^^', upper=False),
            #     "color": "#1F7087",
            #     "src": "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
            #     "title": "Supermffwodel",
            #     "name": "Avatar",
            #     "type": "AvatarBlock",
            #     "thumbnail": "",
            #     "imageIcon": "mdi-face-recognition",
            #     "aspectRatio": ""
            # },

            #  {
            #     "id": f.hexify(text='^^^^', upper=False),
            #     "color": "#1F7087",
            #     "title": "Supermodel",
            #     "name": "Image",
            #     "type": "ImageBlock",
            #     "aspectRatio": "-1.7",
            #     "imageIcon": "image",
            # },
            # {
            #     "id": f.hexify(text='^^^^', upper=False),
            #     "color": "#1F7087",
            #     "name": "Optin",
            #     "type": "OptinBlock",
            #     "block": True,
            #     "thumbnail": "",
            #     "imageIcon": "mdi-email-edit-outline",
            # },
            # {
            #     "id": f.hexify(text='^^^^', upper=False),
            #     "buttonColor": "#1F7087",
            #     "buttonTextcolor": "#1F7087",
            #     "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
            #     "name": "Gallery",
            #     "type": "GalleryBlock",
            #     "social": "instagram",
            #     "block": True,
            #     "galleryImages": [
            #         {
            #             "src":
            #             "https://d33wubrfki0l68.cloudfront.net/adba93920048941f5c368176" +
            #             "54c8ca200dd2bcd1/080af/blog/images/create-web" +
            #             "-extension-vue/header.jpg",
            #             "alt": "iamge1"
            #         },
            #         {"src": "https://picsum.photos/510/300?random", "alt": "image2"},
            #         {"src": "https://picsum.photos/510/300?random", "alt": "image3"}
            #     ]

            # }
        ]
    }

    return data
