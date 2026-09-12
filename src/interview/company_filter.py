def get_companies(df):

    companies = sorted(
        df["Company"]
        .dropna()
        .unique()
        .tolist()
    )

    return companies


def filter_by_company(df, company):

    if company == "All Companies":
        return df

    return df[
        df["Company"].str.lower() == company.lower()
    ]


def filter_by_industry(df, industry):

    if industry == "All Industries":
        return df

    return df[
        df["Industry"].str.lower() == industry.lower()
    ]


def filter_by_role(df, role):

    if role == "All Roles":
        return df

    return df[
        df["Role"].str.lower() == role.lower()
    ]