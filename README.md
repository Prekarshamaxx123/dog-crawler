# 🐕 Dog-Crawler - Worldwide Best Crawling Tool

<div align="center">

![Dog-Crawler](https://img.shields.io/badge/Dog--Crawler-Advanced%20Web%20Crawler-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-green)
![Platform](https://img.shields.io/badge/Platform-Windows%2C%20Linux%2C%20Kali-lightgrey)
![License](https://img.shields.io/badge/License-Educational%20Use-only)

**Advanced Web Crawling Solution with Onion Site Support**

*Powered by PREKASH TECH | WhatsApp: +94721986326*

</div>

## 📖 Table of Contents
- [Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🔧 Usage](#-usage)
- [🌐 Onion Site Support](#-onion-site-support)
- [📊 Crawling Modes](#-crawling-modes)
- [📁 Output Structure](#-output-structure)
- [🛠️ Requirements](#️-requirements)
- [📞 Contact & Support](#-contact--support)
- [⚠️ Disclaimer](#️-disclaimer)

## 🎯 Overview

**Dog-Crawler** is an advanced, multi-threaded web crawling tool designed for comprehensive website reconnaissance and mapping. Built with cutting-edge technology, it supports both surface web and onion sites with dual crawling modes for flexible scanning operations.

```python
# Example: Quick Start
from dog_crawler import DogCrawler

crawler = DogCrawler("https://example.com", mode="fast")
crawler.start_crawling()
```

## ✨ Features

### 🎨 Core Capabilities
- **🌐 Dual Crawling Modes** - FAST 🚀 & ALL 🔍 scanning options
- **🕸️ Onion Site Support** - Complete .onion domain compatibility
- **⚡ Multi-threaded** - High-speed parallel processing
- **🎯 Smart URL Discovery** - Advanced duplicate prevention
- **📁 File Type Categorization** - Automatic file classification
- **🔒 SSL Bypass** - Self-signed certificate support
- **🔍 Enhanced sequential detection** - Response similarity checking
- **🌐 JavaScript site detection** - Auto URL extraction
- **🗺️  Sitemap checking** - Additional URL discovery

### 🔧 Technical Features
- **Colorized Console Output** - Beautiful terminal interface
- **Progress Tracking** - Real-time scanning statistics
- **Error Handling** - Robust network error management
- **Cross-Platform** - Windows, Linux, and Kali Linux compatible
- **No Dependencies** - Easy setup and deployment
- **Patterns Auto-Detected** - Sequential patterns auto-detected and generated

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection
- For onion sites: Tor browser (optional)
- 
<div align="center">
**🛑 Termux 32bit,64bit and Linux 64bit Only Working !! 🛑**
</div>

### Basic Usage
```bash
# Clone or download the script
git clone https://github.com/Prekarshamaxx123/dog-crawler.git
cd dog-crawler

# Create a virtual environment
python3 -m venv prekarsha_env
source prekarsha_env/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the crawler
python dog-crawler.py
```

## 📦 Installation

### Method 1: Direct Download
```bash
# Download the script
wget https://github.com/Prekarshamaxx123/dog-crawler/blob/main/dog-crawler.py

# Install dependencies
pip install requests beautifulsoup4 fake-useragent colorama
```

### Method 2: Git Clone
```bash
git clone https://github.com/Prekarshamaxx123/dog-crawler.git
cd dog-crawler
pip install -r requirements.txt
```

### Requirements File
```txt
requests>=2.28.0
beautifulsoup4>=4.11.0
fake-useragent>=1.1.0
colorama>=0.4.0
urllib3>=1.26.0
```

## 🔧 Usage

### Interactive Mode
```bash
python dog-crawler.py
```

**Follow the prompts:**
1. Enter target URL
2. Choose crawl mode (FAST/ALL)
3. Set thread count (default: 5)
4. Set delay between requests (default: 1s)

### Example Sessions

**Regular Website Scan:**
```bash
> python dog-crawler.py
Enter the website URL: https://example.com
Select Crawl Mode:
[1] FAST 🚀 - Quick scan (Katana-style, limited depth)
[2] ALL 🔍 - Deep complete scan (all pages)
Enter choice (1 or 2): 1
```

**Deep Site Scan:**
```bash
> python dog-crawler.py
Enter the website URL: http://example.onion
Select Crawl Mode:
[1] FAST 🚀 - Quick scan (Katana-style, limited depth)  
[2] ALL 🔍 - Deep complete scan (all pages)
Enter choice (1 or 2): 2
```

## 🌐 Onion Site Support

Dog-Crawler provides seamless onion site crawling capabilities:

### Prerequisites for Onion Sites
1. **Tor Browser** (Recommended)
   - Download from: https://www.torproject.org/
   - Keep Tor browser running during scans

2. **OR Tor Proxy Configuration**
   ```python
   # Manual proxy configuration (if needed)
   proxies = {
       'http': 'socks5h://127.0.0.1:9050',
       'https': 'socks5h://127.0.0.1:9050'
   }
   ```

3. **OR Use Proxychains**
   ```python
   sudo apt install tor
   sudo systemctl start tor
   proxychains4 python dog-crawler.py
   ```

### Onion Site Usage
```bash
# Direct onion site crawling
python dog-crawler.py
# Enter: http://example.onion

# The script automatically:
# - Detects .onion domains
# - Uses appropriate timeouts
# - Disables SSL verification
# - Handles Tor network delays
```
<img width="1426" height="79" alt="Screenshot 2025-11-29 221720" src="https://github.com/user-attachments/assets/7d53aeb9-ff74-4ef3-b219-93a24e53c48a" />
<img width="1572" height="985" alt="Screenshot 2025-11-29 221636" src="https://github.com/user-attachments/assets/0879b4ef-6f3d-430e-9cc0-370bde548d52" />
<img width="1635" height="878" alt="Screenshot 2025-11-29 221612" src="https://github.com/user-attachments/assets/bbe15148-aa6a-4266-a7a6-28b3a9e3af51" />
<img width="1476" height="780" alt="Screenshot 2025-11-29 221558" src="https://github.com/user-attachments/assets/1eac6523-d794-4f3f-ba64-cc0e0d933f5d" />


## 📊 Crawling Modes

### 🚀 FAST Mode (Katana-Style)
- **Purpose**: Quick reconnaissance and initial mapping
- **Depth**: Limited to 2 levels
- **Speed**: Ultra-fast scanning
- **Resources**: Basic file extraction only
- **Use Case**: Initial target assessment

### 🔍 ALL Mode (Complete Scan)  
- **Purpose**: Comprehensive website mapping
- **Depth**: Unlimited crawling depth
- **Speed**: Thorough but slower
- **Resources**: All file types extracted
- **Use Case**: Complete website analysis

### Mode Comparison
| Feature | FAST Mode | ALL Mode |
|---------|-----------|----------|
| Crawling Depth | 2 levels | Unlimited |
| File Extraction | Basic | Comprehensive |
| Speed | 🚀 Very Fast | 🐢 Moderate |
| Resource Usage | Low | High |
| Output Detail | Essential URLs | Complete Map |

## 📁 Output Structure

After each scan, Dog-Crawler creates a comprehensive output directory:

```
dog_crawled_example_com/
├── 📄 all_urls.txt              # All discovered URLs
├── 📄 internal_urls.txt         # Target domain URLs only
├── 📄 external_urls.txt         # External domain URLs
├── 📄 external_domains.txt      # List of external domains
├── 📄 pdf_urls.txt             # PDF documents
├── 📄 png_urls.txt             # PNG images
├── 📄 jpg_urls.txt             # JPG images
├── 📄 css_urls.txt             # CSS files
├── 📄 js_urls.txt              # JavaScript files
├── 📄 [other_file_types].txt   # Additional file types
└── 📄 crawling_summary.txt     # Detailed scan report
```

### Output File Details

**`crawling_summary.txt` Example:**
```txt
=== DOG-CRAWLER SCAN SUMMARY ===
Scan Tool: Dog-Crawler
Powered by: PREKASH TECH
Contact: +94721986326
For: Educational Purposes Only
Crawl Mode: FAST
Base URL: https://example.com
Total Pages Crawled: 45
Total Unique URLs Found: 128
Internal URLs: 89
External URLs Found: 39
Files Found: 23
Scan completed: 2024-01-15 14:30:22
```

## 🛠️ Requirements

### Python Packages
```txt
requests>=2.28.0          # HTTP requests handling
beautifulsoup4>=4.11.0    # HTML parsing
fake-useragent>=1.1.0     # User-Agent rotation
colorama>=0.4.0          # Colored console output
urllib3>=1.26.0          # HTTP client library
```

### System Requirements
- **OS**: Windows 10/11, Linux, Kali Linux
- **Python**: 3.7 or higher
- **RAM**: 2GB minimum, 4GB recommended
- **Storage**: 100MB free space
- **Network**: Stable internet connection

## 📞 Contact & Support

<div align="center">

### 🎯 Developed by PREKASH TECH

**WhatsApp**: +94721986326  
**Email**: slcybertube@gmail.com  
**GitHub**: github.com/Prekarshamaxx123  

</div>

### Support Information
- **Bug Reports**: Create GitHub issues
- **Feature Requests**: Contact via WhatsApp
- **Custom Solutions**: Available upon request
- **Educational Use**: Priority support

### ⚠️ Important Notes
- This tool is for **educational purposes only**
- Always respect `robots.txt` and website terms
- Use responsibly and ethically
- Obtain proper authorization before scanning

## ⚠️ Disclaimer

```text
███████╗███████╗███████╗███████╗
██╔════╝██╔════╝██╔════╝██╔════╝
█████╗  █████╗  █████╗  █████╗  
██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
██║     ███████╗██║     ███████╗
╚═╝     ╚══════╝╚═╝     ╚══════╝
```

**LEGAL DISCLAIMER**: This tool is developed for educational and authorized security testing purposes only. The developers are not responsible for any misuse or damage caused by this program. Users must ensure they have proper authorization before scanning any website or network.

### 🎓 Educational Purpose Only
- Intended for cybersecurity education
- Use in authorized environments only
- Respect privacy and legal boundaries
- Follow ethical hacking guidelines

### 📜 License
This project is licensed for educational use. Commercial use requires explicit permission from the developer.

---

<div align="center">

**🐕 Dog-Crawler - Worldwide Best Crawling Tool**  
*Advanced Web Reconnaissance Solution*

**⭐ Star this repository if you find it helpful!**

</div>

## 🔄 Update Log

### Version 1.0.0
- Initial release with dual crawling modes
- Onion site support
- Comprehensive output system
- Cross-platform compatibility

### Planned Features
- [ ] API integration
- [ ] Report generation (PDF/HTML)
- [ ] Advanced filtering options
- [ ] Plugin system

---

*Last Updated: November 2025*  
*© 2025 PREKASH. All Rights Reserved.*
