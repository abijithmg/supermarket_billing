## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Simulation of Simple Super Market billing with group discount offers

## Installation

To install and run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/abijithmg/supermarket_billing.git`
2. Install pytest `pip install pytest`
3. Run the application: `python app.py`
In case you want to run via docker
1. Install the required dependencies: `brew install --cask docker` or docker desktop
2. Make sure Docker Daemon is running `docker ps`
3. From the project folder, to create build `docker build -t sm-billing .`
4. In order to run the actual program `docker run -t -i sm-billing`

## Unit Testing

1. Make sure pytest is installed 
2. Comment the last line: print(f"Total price: {total_price}")
2. From project folder run `pytest`

## Usage

Once the application is up and running, you can perform the following actions:

Enter the items in the cart [Example: A, AB, CDBA, AAA, BAB etc]:
Sample Input- BAB
Sample Output- Total price: 95


## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
