primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def nearest(lst, n):
    return min(lst, key=lambda x:abs(x-n))
    
for i in range(int(input())):
    lens = int(input())
    st   = input()
    tg   = ""
    for i in st:
        near = nearest(primes,ord(i))
        tg +=  chr(near)
    print(tg)    
    
'''
2
375
AvfmaLgLRpQadLyThsxVzkUqbFOdxfbLGdpBWOwmAnflENlYFbdhNHerHVtZkaPLgMtNQovVHpwGfHJdXXWAhYrhwXKPxtnpxCIsaXVAkcxTpVprFNeOVcnSEsgIvfqXPRSUASSDCvAGrFJCDbzGLFhrMYWALElChmurLrEeQttIWctyhQXzZUVAYuCIZecBJbXMxlMHFbZxJRTSZJmZAwCggGabVsovqBrdmmbCTaIHDfUunLFntfGzodKqoAKwCassKMDybethRaQgegsOawfNCNrIAkECEKpbwElhvWtlZBEZqJQpEkzpiSjrqZZIHbszUxwuWreXkxFKxSAiKoemIqETGVxcCjweKhbyXxhVKCbNTQBKgHD
20
AWGrOwUcFWnghtAyvxSb
CqemaIgISqOaeISgqqSkSqaGOeqeaIGeqCYOqmCmekCOkYGaegOGeqGSqYkaOIgOqOOmqSGqqGeGIeYYYCgYqgqYIOqqmqqCIqaYSCkaqSqSqqGOeOSamSCqgIqeqYOSSSCSSCCqCGqGICCaGIGgqOYYCICkCgmqqIqCeOqqIYaqgOYYSSCYqCIYeaCIaYOqkOGGaYqISSSYImYCqCggGaaSqmqqCqemmaCSaIGCeSqmIGmqeGmeIqmCIqCaqqIOCaeqgSaOgegqOaqeOCOqICkCCCIqaqCkgqYqkYCCYqIOqCkqgSkqqYYIGaqSqqqYqeYkqGIqSCgImemIqCSGSqaCkqeIgaYqgSICaOSOCIgGC
CYGqOqSaGYmggqCqqSa
CqemaIgISqOaeIqSgqqSqkSqaGOeqeaIGeqCYOqmCmekCOkYGaegOGeqGSqYkaOIgOqOOmqSGqqGeGIeYYYCgYqgqYIOqqmqqCIqaYSCkaqSqSqqGOeOSamSCqgIqeqYOSSSCSSCCqCGqGICCaqGIGgqOYYCICkCgmqqIqCeOqqIYaqqgOYqYSSCYqCIYeaCIaYOqkOGGaYqISSSYImYCqCggGaaSqmqqCqemmaCSaIGCeSqmIGmqeGqmeIqmCIqCaqqIOCqaeqgSaOgegqOaqeOCOqICkCCCIqaqCkgqYqkYCCYqIOqCkqqgSkqqYYIGaqqSqqqYqeYkqGIqSCgImemIqCSGSqaCkqeIgaqYqgSICaOSOCIgGC
CYGqOqSaGYmggqCqqqSa

'''
    
        
