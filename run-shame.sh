#! /bin/bash
set -ex
# Target completion date date
finish_date=2021-3-13
# Length in pages
target_thesis_length=110

################################################################################
# You shouldn't have to change this
################################################################################

current_length=$(grep -Eo "\d\d* pages" $1 | awk '{print $1}')
./scripts/shame.py $current_length $finish_date $target_thesis_length
