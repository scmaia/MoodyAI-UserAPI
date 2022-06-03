# Moody AI

Full stack application providing an interface for interaction with an AI chatbot powered by OpenAI API. The user can select the chatbot's mood, whose behaviour is defined by training examples in the backend. User authentication allows users to save the interaction history as well as favorited AI responses. Filters in the frontend allow for easy browsing of the chatbot's past responses.

Demo: [https://moodyai.netlify.app/](https://moodyai.netlify.app/)

Frontend Repo: [https://github.com/scmaia/MoodyAI-FE](https://github.com/scmaia/MoodyAI-FE)
Backend Repo: [https://github.com/scmaia/MoodyAI-UserAPI](https://github.com/scmaia/MoodyAI-UserAPI)

## Tech Stack

### Frontend
- Typescript
- React.js
- Fetch API
- SASS & BEM

### Backend
- Python
- Django
- Django Rest Frameword


## Features

### Frontend
- Mood selector
- Option to favorite responses
- Filter per mood and/or favorites
- Responsive Design
- Tested for accessibility
- Vintage UI (own design & assets)

### Backend
- User Authentication
- Handles API calls to OpenAI


## Installation

Install MoodyAI-FE with npm in project's root folder

```bash
  npm install
```

Install MoodyAI-API with pip in project's root folder

```bash
  pip install
```

## Environment Variables

For MoodyAI-API, you will need to add the following environment variables to your .env file

`OPENAI_KEY`

## Screenshots

![App Screenshot](./public/moodyAI.JPG)


## Accessibility

Project tested with Axe DevTools.

![App Screenshot](./public/axe-passed.JPG)

## Production checklist

If I had more time to work on this project, I would:

- Add share button
- Add delete button for individual responses as well as delete all
- Implement unit tests as well as end-to-end tests.
- Limit CORS domains. Right now it is irrestricted.

## Authors

- [@Sara Maia](http://www.saramaia.me)

## Acknowledgements

- [OpenAI](https://beta.openai.com/)
