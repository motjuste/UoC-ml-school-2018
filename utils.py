import requests


def download_file(from_url, to_path, chunk_size=1024):
    r = requests.get(from_url, stream=True)
    with open(to_path, "wb") as f:
        print("Downloading...", end=' ', flush=True)
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)

    print("DONE", flush=True)
    return to_path