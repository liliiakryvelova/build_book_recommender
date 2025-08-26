# Music Recommendation Systems Comparison

A comprehensive comparison of different recommendation system approaches using a custom music dataset.

## 📊 Project Overview

This project demonstrates and compares four different types of recommendation systems:

1. **Content-Based Filtering** - Recommends music based on genre similarities
2. **Collaborative Filtering** - Recommends based on user behavior patterns
3. **Matrix Factorization** - Advanced collaborative filtering using NMF
4. **Hybrid System** - Combines content-based and collaborative approaches

## 🎵 Dataset

The project uses a custom-generated music dataset (`music_dataset.csv`) containing:
- **196 entries** covering artist-genre relationships
- **79 unique artists** across multiple music categories
- **78 unique genres** including Pop, Rock, Hip-Hop, Jazz, Classical, and more

### Featured Artists
- Taylor Swift, The Beatles, Drake, Miles Davis
- Beyoncé, Ed Sheeran, Kendrick Lamar, Mozart
- And many more across different genres and eras

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Running the Analysis
1. Clone this repository
2. Navigate to the project directory
3. Open the Jupyter notebook:
   ```bash
   jupyter notebook music_recommendation_systems_comparison.ipynb
   ```

## 📁 Project Structure

```
build_book_recommender/
├── README.md                                    # Project documentation
├── music_dataset.py                            # Dataset generation script
├── music_dataset.csv                           # Generated music dataset
├── music_recommendation_systems_comparison.ipynb   # Main analysis notebook
└── requirements.txt                             # Python dependencies
```

## 🔍 Analysis Features

### Content-Based Filtering
- Uses TF-IDF vectorization on music genres
- Calculates cosine similarity between artists
- Provides transparent, explainable recommendations

### Collaborative Filtering
- Simulates user-artist rating data
- User-based collaborative filtering approach
- Handles user preference patterns

### Matrix Factorization
- Non-negative Matrix Factorization (NMF)
- Captures latent factors in user-artist relationships
- Provides RMSE evaluation metrics

### Hybrid System
- Combines content-based and collaborative approaches
- Configurable weighting between methods
- Comprehensive recommendation explanations

## 📈 Key Results

- **Diversity Analysis**: Comparison of unique artists recommended by each system
- **Coverage Metrics**: Percentage of total artists covered by recommendations
- **Performance Evaluation**: RMSE scores and system complexity analysis
- **Visual Comparisons**: Charts showing genre distributions and recommendation patterns

## 🎯 Conclusions

Each recommendation system has distinct advantages:
- **Content-Based**: Best for new users, transparent recommendations
- **Collaborative**: Excellent for discovering new genres, community-driven
- **Matrix Factorization**: Superior accuracy with large datasets
- **Hybrid**: Balanced approach combining multiple strengths

## 🛠️ Technical Implementation

- **Language**: Python 3.9+
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Environment**: Jupyter Notebook
- **Algorithms**: TF-IDF, Cosine Similarity, NMF, User-Based CF

## 📚 Learning Outcomes

This project demonstrates:
- Different recommendation system architectures
- Evaluation methodologies for recommendation systems
- Data generation and preprocessing techniques
- Comparative analysis of ML approaches
- Real-world application considerations

## 🤝 Contributing

Feel free to fork this repository and experiment with:
- Different similarity metrics
- Alternative matrix factorization techniques
- Deep learning approaches
- Additional evaluation metrics
- Real music datasets (Spotify API, Last.fm, etc.)

## 📄 License

This project is open source and available under the MIT License.
