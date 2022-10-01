# SUEP-health-report

## Usage

### Local environment

```bash
cp envconfig.example.py envconfig.py
vim envconfig.py                      # please edit the configuration
pip install -r requirements.txt
python main.py
```

### Docker

```bash
cp envconfig.example.py envconfig.py
vim envconfig.py                      # please edit the configuration
docker build -t suep-health-report .
docker run -it suep-health-report
```

### GitHub Actions

1. Copy the configuration file to Actions secrets in your repository and edit it.
2. Name it `CONFIG` and save it.
3. Run the workflow.

Please follow the [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) if you use GitHub Actions.

## Configuration

| Variable      | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| username      | 8-digit student ID in string                                |
| password      | password at [IDS](https://ids.shiep.edu.cn)                 |
| wait_time     | Maximum time to wait for the page to load, in seconds       |
| confirm_time  | Time to wait for the user to confirm the report, in seconds |
| headless      | Whether to run the browser in headless mode                 |
| fullscreen    | Whether to run the browser in fullscreen mode               |
| quit_on_error | Whether to quit the program when an error occurs            |
| private       | Reduce the amount of information output                     |

## License

AGPLv3

This program is provided as is, without warranty or liability, please see the LICENSE file for more details.
By using this program, you agree to the terms of the license.
