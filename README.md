# 🎬 Movie Recommender System

A simple web app built using **Streamlit** that recommends similar movies based on your selected favorite. The system uses a content-based recommendation approach powered by a similarity matrix.

 **Live App**: [Click here to try it out!](https://movie-recommender-system-hval.onrender.com)

---

## 🚀 Features

- Select a movie and get 5 similar movie recommendations
- Movie posters are fetched from **TMDB API**
- Lightweight UI using **Streamlit**
- Uses a precomputed **similarity matrix** for fast lookup

---

## 🧠 How It Works

- `movies_dict.pkl`: Contains metadata (movie titles and IDs)
- `similarity.pbz2`: Compressed matrix of similarity scores between movies
- Recommendations are based on similarity score (cosine similarity or similar logic)

---

## 🔧 Tech Stack

- 🐍 Python 3.x
- 🖥️ Streamlit
- 📦 Pandas, Requests, Pickle, BZ2 (or Joblib/GZip)
- 🎥 TMDB API

---

## 📁 Project Structure

|── app.py # Main Streamlit app
├── movies_dict.pkl # Movie metadata
├── similarity.pbz2 # Compressed similarity matrix
├── requirements.txt # Dependencies
├── README.md # This file


---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system

✅ 2. Install Dependencies
pip install -r requirements.txt

✅ 3. Run the App

streamlit run app.py

🔑 TMDB API
url = f"https://api.themoviedb.org/3/movie/{{movie_id}}?api_key=YOUR_API_KEY"
with your actual TMDB API key.

🙋‍♂️ Author
Sourabh Kumar

