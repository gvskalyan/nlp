import json
import sys
import logging
import datetime
import os.path as op

from allennlp.commands import main

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python train.py <input_config_file>")
        sys.exit(0)

    config_file = sys.argv[1]

    # Specify overrides
    overrides = json.dumps({
        "iterator": {"batch_size": 64},
        "trainer": {"cuda_device": 0}
    })

    # Specify output dir according to current time
    experiment_name = op.splitext(op.basename(config_file))[0]
    time_stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    serialization_dir = "./output_%s_%s" % (experiment_name, time_stamp) 

    # Assemble the command into sys.argv
    sys.argv = [
        "allennlp",  # command name, not used by main
        "train",
        config_file,
        "-s", serialization_dir,
        "--include-package", "hznlp",
        "-o", overrides,
    ]

    logging.basicConfig(level=logging.INFO)

    main()
