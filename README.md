# My Zootopia

My Zootopia is a Python project that generates an HTML website with information about animals.

The application fetches animal data from the API Ninjas Animals API and creates a webpage displaying information such as diet, location, and type.

## Installation

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API key:

```text
API_KEY='your_api_key'
```

## Usage

Run the program:

```bash
python3 animals_web_generator.py
```

Enter the name of an animal when prompted.

Example:

```text
Enter a name of an animal: Fox
```

The program will generate an `animals.html` file containing information about the selected animal.

## Technologies Used

* Python
* Requests
* Python Dotenv
* API Ninjas Animals API

## Contributing

Contributions are welcome. Feel free to fork the repository and submit improvements.
