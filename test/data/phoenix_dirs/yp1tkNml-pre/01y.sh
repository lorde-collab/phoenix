#!/bin/bash
sub_array_for_cmdfile.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-RefSeq.nm.sh --log-tpl /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-01-mapping/logs/%W.%J.%I.txt -app mapping-rna-align-rsnm
sub_array_for_cmdfile.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-RefSeq.alt_exon.sh --log-tpl /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-01-mapping/logs/%W.%J.%I.txt -app mapping-rna-align-rsae
sub_array_for_cmdfile.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-AceView.nm.sh --log-tpl /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-01-mapping/logs/%W.%J.%I.txt -app mapping-rna-align-avnm
sub_array_for_cmdfile.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-WG.sh --log-tpl /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-01-mapping/logs/%W.%J.%I.txt -app mapping-rna-align-wg
sub_array_for_cmdfile.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-STAR.sh --log-tpl /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-01-mapping/logs/%W.%J.%I.txt -app mapping-rna-align-star
