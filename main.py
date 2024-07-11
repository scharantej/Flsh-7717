
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    flowers = [
        {
            "name": "Rose",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Rosa_chinensis_var._semperflorens.jpg/1200px-Rosa_chinensis_var._semperflorens.jpg",
            "description": "The rose is a woody perennial flowering plant of the genus Rosa, within the family Rosaceae."
        },
        {
            "name": "Lily",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Lilium_lancifolium_thunb.jpg/1200px-Lilium_lancifolium_thunb.jpg",
            "description": "The lily is a flowering plant with large, trumpet-shaped flowers."
        },
        {
            "name": "Sunflower",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Helianthus_annuus_Florets.jpg/1200px-Helianthus_annuus_Florets.jpg",
            "description": "The sunflower is a large, annual plant with a single, large flower head."
        }
    ]
    return render_template('index.html', flowers=flowers)

if __name__ == '__main__':
    app.run(debug=True)
