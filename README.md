# Omni-GPT

<img src="assets/banner.png">

Have you heard of Auto-GPT? Chances are yes..
Omni-GPT is my own *extremely* simplified version of it, which can
take input from the user and generate a static HTML-Website.

It's a lightweight alternative of Auto-GPT.

## Get started

1. To get started, firstly, clone the repository:

```bash
git clone https://github.com/FujiwaraChoki/Omni-GPT.git
```

2. Now you need to run the docker container, simply run it using the Dev Containers Extension from VS Code.

3. Copy .env.template file and then change contents
```bash
cp .env.template .env
```

4. Run file
```bash
python3 main.py
```

5. Start creating websites! :)

## Example

You can visit the generated example [here](https://example-gilt.vercel.app).

This was the prompt used to generate this site:

```
A website that allows users to interact with ChatGPT through the OpenAI API, with fetch() requests in JavaScript. The user has to provide his own API Key through the frontend. The user should be able to enter a prompt and then after fetching, the website should display ChatGPT's answer. Use TailwindCSS classes.
```
