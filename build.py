import re
import subprocess

from fastapi import FastAPI
import json
import os
app = FastAPI()


@app.get("/build")
async def build(username, site_id=None):
    output = subprocess.check_call(
        "gridsome build",
        stderr=subprocess.STDOUT, shell=True, encoding="utf-8")
    return
    if not site_id:
        website_name = f"ontario-{username}"
        #     output = subprocess.check_output(
        #         f"echo | netlify sites:list",
        #         stderr=subprocess.STDOUT, shell=True, encoding="utf-8")
        #     pattern = rf"{website_name}\s-\s([\w-]+)"
        #     r = re.findall(pattern, output)
        #     if r:
        #         site_id = r[0]
        #         # print(os.environ['NETLIFY_SITE_ID'])
        # else:
        output = subprocess.check_output(
            f"echo | netlify sites:create --name={website_name}",
            stderr=subprocess.STDOUT, shell=True, encoding="utf-8")
        site_id = re.findall(r'Site ID:\s+([\w-]+)', output)
    os.environ['NETLIFY_SITE_ID'] = site_id
    output = subprocess.check_output('echo "dist" |netlify deploy --prod',
                                     stderr=subprocess.STDOUT, shell=True, encoding="utf-8")
    return {"message": "website deployed"}
    # js = json.loads(output)
    # try:
    #     output = subprocess.check_output(
    #         f"echo | netlify sites:create --name={website_name}",
    #         stderr=subprocess.STDOUT, shell=True, encoding="utf-8")
    #     site_id = re.findall(r'Site ID:\s+([\w-]+)', output)
    # return {"message": site_id}


@app.get("/layouts")
def layouts(username):

    data = {
        "community":
        {
            "user_id":
            "community",
            "name":
            "community",
            "paid": True,
            "bio":
            f.paragraph(nb_sentences=5,
                        variable_nb_sentences=True,
                        ext_word_list=None),
            "app_bar_color": "amber",

            "layout": [
                {
                    "id": f.hexify(text='^^^^', upper=False),
                    "color": "#1F7087",
                    "title": "Supermodel",
                    "name": "Image",
                    "type": "ImageBlock",
                    "aspectRatio": "-1.7",
                    "imageIcon": "image",
                    "hidden": False
                },
                {
                    "id": f.hexify(text='^^^^', upper=False),
                    "type": "PatreonBlock",
                    "PatreonAccountID": "",
                    "hidden": False
                },
                {
                    "id": f.hexify(text='^^^^', upper=False),
                    "type": "SpotifyBlock",
                    "SpotifyAccountID": "26dSoYclwsYLMAKD3tpOr4",
                    "hidden": True
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
                    "galleryImages": {"src": "", "alt": ""},
                    "hidden": False
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
                    "hidden": False
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
                    "hidden": False
                },
                {
                    "id": f.hexify(text='^^^^', upper=False),
                    "color": "#1F7087",
                    "src": "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
                    "name": "Divider",
                    "type": "DividerBlock",
                    "hidden": False
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
                    "hidden": False
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
                    "hidden": False
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
        }}

    return data.get(username)
