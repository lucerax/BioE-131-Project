Description of output files from ScanFold for the SARS-CoV-2 genome. Users can load several of these, marked “Y” in the IGV column, directly into the IGV desktop app (tested for versions 2.5.3 to 2.61 as well as IGV.js).

File name	IGV	Description
RawScanData.out		Raw output of ScanFold-Scan. Traditional scanning window output, showing all metrics calculated per window including MFE, z-score, p-value, dot-bracket structure, and centroid structure.
MFE.wig	Y	These are “wig” format files corresponding to values from the ScanFold-Scan output.
ED.wig	Y	
z-scores.wig	Y	
p-values.wig	Y	
ScanFold_BPs.bp	Y	IGV base pair track. The “.bp” format describes the connections between nucleotides and the header contains information such as the color used to depict the arc. For proper loading in IGV, IGV must first be loaded with the “.input.fa” and “.fai” files below.
ScanFold_BPs.WithCompetingPairs.bp	Y	IGV base pair track. 
FinalZavg.wig	Y	This is another “wig” format file which reports the Zavg values corresponding to the arrangements depicted in the “.bp” track above.
NC_045512.fa	Y	This is the FASTA file containing the sequence which was scanned (NC_045512.2)
NC_045512.fai	Y	This is the index file for the FASTA file above, and is used by IGV.
NC_045512.-1_BPs.ct	Y	Structure model files showing base pair arrangments whose Zavg scores are less than the filter value stated in extension. The “CT” files are connectivity files and can be opened in programs such as VARNA, IGV, and RNAstructure.
NC_045512.-2_BPs.ct	Y	
NC_045512.ALL_BPs.ct	Y	
		
FinalPartners.txt
		This is output from ScanFold-Fold and list the “best” arrangments for each nucleotide sequence as well as the corresponding average metrics observed.
ScanFold.log		Raw output of ScanFold-Fold. This will give the list of all base pairs predicted for each nucleotide, the number of windows each are observed in, and the average metrics for each.
ExtractedStructures.txt		This file contains all structures which contained at least one base pair with a Zavg of < -1. The sequences comprising these structures are then refolded individually and z-scores and ensemble diversity are recalculated for the motif.
