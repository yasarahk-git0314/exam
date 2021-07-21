### Problem:
- You have a vendor that delivers 2 files (`SOURCEDATA.TXT`, `SOURCECOLUMNS.txt`) every day at 6AM UTC. These files will land in `data/source/` for processing. For this assessment, you are provided the files in the `data/source/` path as if they were already delivered from the vendor.
- One file contains the raw pipe-delimited data (`SOURCEDATA.TXT`) without a header row.
- The other file (`SOURCECOLUMNS.txt`) contains the headers in the same order as the data in `SOURCEDATA.txt`, but each header is a separate row. 
(e.g. the first column in `SOURCEDATA.txt` is `Order ID`, the next is `Order Date` and so on.)

### Your requirements:
- Make your own copy of this repo on GitHub.
>I would recommend not forking the repository... unless you want the possibility of another candidate to get some great ideas from your solution, as a forked solution will be directly linked to this on GitHub. :)
- Write a program that shall use `src/main.py` as the entrypoint.
- The program shall take the data from both files, transform the data into a single __CSV__ file with both header row and data in a __comma-separated format__, and finally loads it into `/data/destination` by using the `load_csv()` method in `SomeStorageLibrary` located in `src/some_storage_library.py`.
- Provide a link to your solution when you are complete.

> Note: I will simply be executing `python main.py` with the `src/` directory as the current working directory. Whatever happens after that is up to you- just make sure the `.csv` you create exists in `data/destination/` after this runs.

> Note: use Python >= 3.7 to solve and do not use any other packages or dependencies (e.g. Pandas). The goal is to show us your coding style
and see how you would approach the problem using plain Python. 