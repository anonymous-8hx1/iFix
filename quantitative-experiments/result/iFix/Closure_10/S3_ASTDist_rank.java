9: return anyResultsMatch( n , MAY_BE_STRING_PREDICATE ) ;
10: return mayBeStringHelper( n ) ;
11: return mayBeString( n , false ) ;
12: return( mayBeStringHelper( n ) ) ;
27: return mayBeStringHelper( n ) ? true : false ;
27: return( mayBeStringHelper( n ) && recurse ) ;
27: return( recurse && mayBeStringHelper( n ) ) ;
27: return mayBeString( n ,( boolean ) false ) ;
27: return mayBeStringHelper(( Node ) n ) ;
27: return( mayBeString( n , false ) ) ;
27: return recurse && mayBeStringHelper( n ) ;
