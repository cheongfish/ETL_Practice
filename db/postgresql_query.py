queries = {"make_table_query" : ["""
                                    CREATE TABLE IF NOT EXISTS "TEST1"(
                                        "ID" SERIAL PRIMARY KEY,
                                        "Name" VARCHAR(50) ,
                                        "CountryCode" VARCHAR(50) ,
                                        "District" VARCHAR(355) ,
                                        "Population" INTEGER
                                                        );
                                """,
                                """
                                    CREATE TABLE IF NOT EXISTS "TEST2"(
                                        "ID" SERIAL PRIMARY KEY,
                                        "Name" VARCHAR(50) ,
                                        "CountryCode" VARCHAR(50) ,
                                        "District" VARCHAR(355) ,
                                        "Population" INTEGER
                                                        );
                                """],
                          
            "INSERT_query" : """
                                INSERT INTO "TEST1" ("ID","Name","CountryCode","District","Population")
                                VALUES (
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s
                                        ) ; 
                            """
            }