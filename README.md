## About
Serene CMS is a YAML based CMS using which you can convert YAML based input files into static HTML content. You can then host the static content on an object storage service like AWS S3, Cloudflare R2, etc. 
- Supports multiple data containers, which are used to hold various representations of data, like text, images, tables, subsections, etc.
- Gives you the ability to add custom HTML templates yourself.

## Target audience
If your have a basic understanding of Yaml, HTML, CSS and Command Line interface, and wish to host a static website **cost-effectively**, then this tool is for you.

Using CDNs will further reduce your object storage expenses with providers like S3 which charge based on request count.

## Quick Start

### Setup your project

#### Clone the project
```shell
git clone 
```

#### Initialize  new project
```shell
./create-project.sh --name hello-world --path /path/to/content_dir
```

### Add pages to your site
#### Navigate to your content directory
```shell
cd /path/to/content_dir
```

#### Create a subpage
```shell
mkdir content/my_page_1
touch content/my_page_1/index.yaml
```

#### Add content to your new subpage
```yaml
title: Subpage 1
author: Nar
publish_date: 2025-01-01
template:
body:
  - type: section-heading
    content:
      - Section 1
  - type: text
    content:
      - Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

#### Generate static pages
```shell
./gen.sh --path /path/to/content
```

### Access your static content
#### Navigate to your project's static directory
```shell
cd /path/to/content_dir/static
```

#### Start a static file server
```shell
python3 -m http.server --bind 0.0.0.0 8080
```

#### Open the site in your browser
```text
http://127.0.0.1:8080
```

## Available content types

### Text
```yaml
  - type: text
    content:
      - This is paragraph 1
      - This is paragraph 2
```

### Stanza
This differs from `text` type by considering all the lines under content as a single stanza. It is suitable for a poetry like layout.
```yaml
  - type: text-stanza
    content:
      - This is line 1
      - This is line 2
```

### Section heading
```yaml
  - type: section-heading
    content:
      - Section 1
```

### Sub-Section heading
```yaml
  - type: subsection-heading
    content:
      - Section 1
```

### Table
```yaml
    - type: table
      content:
          - - Column heading 1
            - Column heading 2
            - Column heading 3
    
          - - Row 1 Col 1
            - Row 1 Col 2
            - Row 1 Col 3
```

### Unordered List
```yaml
  - type: list-unordered
    content:
      - This is item 1 in an unordered list
      - This is item 2 in an unordered list
```

### Ordered List
```yaml
  - type: list-ordered
    content:
      - This is item 1 in an ordered list
      - This is item 2 in an ordered list
```

### Image
```yaml
  - type: image
    url: /assets/images/crab.jpg
    width: 420
    height: 570
    caption: "[From Wikipedia] Crabs are decapod crustaceans of the infraorder Brachyura"
```