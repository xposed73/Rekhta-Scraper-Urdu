# Rekhta Scraper Urdu

A Python web scraper designed to extract Urdu poetry (ghazals) from [Rekhta.org](https://www.rekhta.org), one of the largest online repositories of Urdu literature.

## 🌟 Features

- **Urdu Poetry Extraction**: Automatically extracts Urdu verses from Rekhta.org ghazal pages
- **Text Cleaning**: Removes HTML artifacts and normalizes text formatting
- **Unicode Support**: Full support for Urdu Unicode characters (Arabic script)
- **Simple Output**: Saves extracted verses to a clean text file
- **Error Handling**: Robust error handling with informative messages

## 📋 Prerequisites

- Python 3.13 or higher
- Internet connection to access Rekhta.org

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/xposed73/Rekhta-Scraper-Urdu.git
   cd rekhta-scraper-urdu
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

### Installing uv

If you don't have `uv` installed, you can install it using one of these methods:

**On Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**On macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Using pip:**
```bash
pip install uv
```


## 📖 Usage

### Basic Usage

Run the scraper with the default URL (Allama Iqbal's ghazal):

```bash
uv run app.py
```

The script will:
1. Fetch the ghazal from Rekhta.org
2. Extract all Urdu verses
3. Save them to `ghazal.txt`

### Custom URL

To scrape a different ghazal, modify the `url` variable in `app.py`:

```python
url = "https://www.rekhta.org/ghazals/your-ghazal-url-here"
```

### Output

The extracted verses are saved to `ghazal.txt` in UTF-8 encoding, with each verse on a separate line.

Example output:
```
ستاروں سے آگے جہاں اور بھی ہیں
ابھی عشق کے امتحاں اور بھی ہیں
تہی زندگی سے نہیں یہ فضائیں
...
```

## 🛠️ How It Works

1. **Web Scraping**: Uses `requests` and `BeautifulSoup` to fetch and parse HTML content
2. **Text Extraction**: Identifies Urdu text blocks using CSS selectors
3. **Text Cleaning**: Removes HTML entities and normalizes whitespace
4. **Unicode Detection**: Uses regex patterns to identify Urdu/Arabic script
5. **File Output**: Saves clean verses to a text file

## 📁 Project Structure

```
rekhta-scraper/
├── app.py              # Main scraper script
├── ghazal.txt          # Output file (generated)
├── pyproject.toml      # Project configuration
├── uv.lock            # Dependency lock file
└── README.md          # This file
```

## 🔧 Dependencies

- **requests**: HTTP library for web requests
- **beautifulsoup4**: HTML parsing and extraction
- **re**: Regular expressions for text processing

## ⚠️ Important Notes

- **Rate Limiting**: Be respectful of Rekhta.org's servers. Don't make too many requests in quick succession.
- **Terms of Service**: Ensure your usage complies with Rekhta.org's terms of service.
- **Educational Use**: This tool is intended for educational and research purposes.

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Bug Reports**: Report issues with specific URLs or error messages
2. **Feature Requests**: Suggest improvements or new features
3. **Code Improvements**: Submit pull requests for better code organization
4. **Documentation**: Help improve this README or add code comments

## 📝 License

This project is open source. Please ensure your usage complies with Rekhta.org's terms of service.

## 🙏 Acknowledgments

- [Rekhta.org](https://www.rekhta.org) for providing access to Urdu literature
- The Urdu poetry community for preserving and sharing this beautiful literary tradition

## 🔗 Related Links

- [Rekhta.org](https://www.rekhta.org) - The source website
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [Requests Documentation](https://requests.readthedocs.io/)

---

**Note**: This scraper is designed for educational purposes. Please respect the source website's robots.txt and terms of service when using this tool.

## 🙏 Support My Work

If you find this project helpful, consider supporting it by donating via UPI.

![Donate via UPI](https://raw.githubusercontent.com/xposed73/YTDL-python/main/upi-donation.png)

Thank you for your support! ❤️

