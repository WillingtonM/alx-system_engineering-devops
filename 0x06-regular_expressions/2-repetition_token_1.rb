#!/usr/bin/env ruby
# This matched str with h followed by 0 or
# 1 occurence of b and then tn

puts ARGV[0].scan(/hb?tn/).join

