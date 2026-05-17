import argparse
from ecg_utils import process_dicom_directory


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
        help="Input DICOM directory"
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Output directory"
    )

    parser.add_argument(
        "--recursive",
        default=True,
        help="Whether to search subdirectories"
    )

    parser.add_argument(
        "--verbose",
        default=False,
        help="Whether to print output messages"
    )

    args = parser.parse_args()

    process_dicom_directory(
        dicom_dir=args.input,
        output_dir=args.output,
        recursive=args.recursive,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()
