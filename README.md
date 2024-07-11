## Flask Application Design
### HTML Files
- `index.html`: The main page of the website that present the content of a flower catalog.
```html
<!DOCTYPE html>
<html>
<head>
  <title>Flower Catalog</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQh58iYOTvQjts2HMCs1559EdU56356eaLLqFAGrQ5391iGkX71p" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <h1>Flower Catalog</h1>
    <div class="row">
      {% for flower in flowers %}
      <div class="col-sm-4">
        <img src="{{ flower.image_url }}" alt="{{ flower.name }}">
        <h3>{{ flower.name }}</h3>
        <p>{{ flower.description }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
</body>
</html>
```

### Routes
- `/`: Displays the main page, `index.html`
```python
@app.route('/')
def index():
    flowers = get_flowers()
    return render_template('index.html', flowers=flowers)
```