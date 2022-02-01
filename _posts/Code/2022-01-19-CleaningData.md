---
layout:	default
title:	"Cleaning the Data"
category:	code
date:	2022-01-19 11:30:00 -0000
permalink:	/code/Python/CleaningData
---

### Screening and converting datatypes
- Some variables may be stored as strings instead of the desired integer, float, datetime, boolean, or category datatype.
- To strip specific text from the data, such as a string '$' before the integer value, use `df['Money_column'].str.strip('$')`. 
- Now the `Money_column` can be converted into int format by using the method `.astype('int')`, and similar process follows  for other screening purposes.
- An `assert df['Money_column'].dtype == 'int'` statement will give out an `AssertionError` if the datatype is not int, for added security on the processing of the data.

### Dropping inconsistent, duplicate data in catogorical data
- After spotting a insoncistent value in a categorical data for example which should not exceed 10, that data can be dropped using `df.dop().index` method. For example, `data_frame.drop(data_frame[data_frame['Categorical_col']>10].index, inplace=True)` will drop the values in `Categorical_col` column that are above 10, without creating a different object.
- **Duplicate data** can be visualized by using `df.duplicated()` method which when stored in a variable can be used to see specific duplicated rows after passing that variable as an argument for the DataFrame.
   * Syntax = `duplicates = df.duplicated(subset = column_names,keep = False)`, will store duplicates in the variable `duplicates`. the argument `subset` is to provide column name as an id to look for duplicates, and `keep` argument can either be `first` to keep the first, `last` for last, or `False` to keep all duplicate values
   * The duplicated dataset can be sorted using `.sort_values()` method and can be treated by either dropping values completely using `.drop_duplicates(inplace=True)` to directly replace duplicates inside the dataframe without creating a new object, or the values can be treated using `.gropupby()` and `.agg()` methods
   * For example, `stats = {'height': 'max','weight':'mean'}` can be called as in the `.agg()` method `data.groupby(by = 'Column_names').agg(stats).reset_index()` to take max of `height` column and `mean` of the weight column. Dataframe can be checked for duplication after this.
- **Text inconsistencies**
  * Inconsitent columns can be seen by creating a Boolean column of the condition that needs to be checked. Ex, `inconsitent_col = df['number']**2== df['square']` which creates a Boolean for rows where the manual square of the number does not equal the DataFrame column corresponding to `square` column. Thus, `df[inconsistent_col]` will display all data of the inconsistent columns, and `df[~inconsistent_col]` displays all other columns (consistent columns)
  * Categorical data inconsitent values can be looked at by converting all text into either upper or lower case using `df['col].str.upper() or df['col].str.lower()` method and the unique values in a columns can beseen by using `.unique()` method
  * Any white spaces around the text can be removed by passing no argument to the `df['col'].str.strip()` method.
  * Leftover inconsistencies or new groups can be created by creating a dictionary which maps the inconsistent text with a new one. For example, `map = {'eur': 'Europe','usa': 'USA'}` can be used as `data['col] = data['col'].replace(map)` to resolve the inconsistency.
  * New categorical data can also be created using `pd.qcut()` or `pd.cut()` function. 
  ```
  range = [0, 20 , 80, np.inf] # extents of the bins desired
  names = ['0-20','20-80,'80+'] # names of the bins
  data['category'] = pd.cut(data[number],bins=range,labels=names)
  ```
  * This creates the desired categories. `pd.qcut()` also works in a similar way but requires setting the number of bins instead of ranges using the parameter `q=n`
- **Datetime inconsistencies**
  * Need to `import datetime as dt`
  * A specific column can be converted to datetime format using pandas `pd.to_datetime(df['Date_column'],infer_datetime_format = True, errors = 'coerce')` function. `infer_datetime_format` parameter attempts to infer format for each date, `errors` return `NaT` for rows where the conversion failed.
  * Then a year, month, or the date can be extracted using `df['Date_column'].dt.year` and so on. 
  * Today's date can be extracted by `dt.date.today()`
- **Missing data**
  * Find and inspect missing data columns using `df['col'].isna().sum()` method calls which compute sum along each column to display the total missing values for each column. 
  * The package `import missingno as msno` has excellent visual ways to inspect the dataframe by `msno.matrix(df)`, which then plots each column and displays missing values for the column in the scatter plot. Then, if there are any relational inconsistencies in the missing data (such as data missing for old people), the DataFrame can be sorted (using `.sort_values(by='col')` method) and the missing values be filled.
  * Filling missing data can be done by `df.fillna({'col':df['col'].mean()})` method.
- **String Similarity or Record Linkage**
  * Text such as "reading" and "reeding" have minimum edit distance of 1 (substitution). Other possible options for editing are deletion, insertion, substitution, and transportation. Least minimum distance indicates the closeness of the text to each other.
  * Many algorithms exist to calculate this minimum distance, with levenshtein algroithm the popular:
  
  | Algorithm | Operations|
  |---|---|
  |Damerau-Levenshtein | insertion, substitution, deletion, transportation|
  |*Levenshtein*| *insertion, substitution, deletion*|
  |Hamming | substitution only|
  |Jaro distance | traansportation only|
  |...| ...|

  * `fuzzywuzzy` package does this process and calculates a ratio of closeness of two texts
  * `from fuzzywuzzy import fuzz`, `fuzz.WRatio('Reading','Reeding')` gives a value of 86, indicating a high match.
  * Comparison of arrays can be done using `from fuzzywuzzy import process`, where `process.extract("String to compare",data["string column"],limit=len(data["string column"])` creates a tuple for each column with Column string as first value, WRatio value as second, and third value is index (if data is a list) or key  (if data is a dict). Limit is an integer value which indicates the maximum number of outputs.
- **Linking DataFrames**
  * The package `import recordlinkage` is beautiful to link two dataframes which have similar but not unique column identifiers. For example, dataset with slightly different label for the measurement value, or address
  * The procedure involves first creating an indexing object:
  ```
  indexer = recordlinkage.Index() # Create indexing object
  
  # Generate pairs blocked on 'state'
  index.block('State') 
  pairs = indexer.index(df_1,df_2) 
  ``` 
  * Next step is to generate a `Compare` object:
  ```
  comp_cl = recordlinkage.Compare()
  # For exact matches
  comp_cl.exact('string_1','string_1',label='string_1')
  comp_cl.exact('string_2','string_2;',label='string_2')
  # For similar matches
  comp_cl.tring('name','name',threshold=0.8,label='name')

  # Finding matches
  potential_matches = compare_cl.compute(pairs, df_1,df_2) # This creates a multiIndex DataFrame (first index for df_1,second index for df_2) and a boolean 1 or 0 for resspective columns being compared
  ```
  * Last step involves linking the data:
  ```
  # Isolating matches based on a match criteria
  
  matches = potential_matches[potential_matches.sum(axis=1)==3] # Meaning all column values compared should match to create this subset of potential matches

  duplicate_rows = matches.index.get_level_values(1) # 1 being the index of second df_2 Dataframe

  df_2_duplicates = df_2[df_2.index.isin(duplicate_rows)]
  df_2_non_duplicates = df_2[~df_2.index.isin(duplicate_rows)]

  # Linking the Dataframes:
  full_dfs = df_1.append(df_2_non_duplicates)
  ```
  
