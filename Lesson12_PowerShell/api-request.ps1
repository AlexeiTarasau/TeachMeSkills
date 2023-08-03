function Get-SWAPIResource {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ResourceUrl
    )

    try {
        # create object
        $request = [System.Net.WebRequest]::Create($ResourceUrl)
        $request.Method = "GET"

        # Sending a request and receiving a response
        $response = $request.GetResponse()

        try {
            # Reading data from a response
            $stream = $response.GetResponseStream()
            $reader = New-Object System.IO.StreamReader($stream)
            $responseContent = $reader.ReadToEnd()

            # Closing threads
            $reader.Close()
            $stream.Close()

            # Return received data
            return $responseContent
        }
        finally {
            $response.Close()
        }
    }
    catch {
        Write-Error "Error while executing request: $_"
    }
}

# Calling a function to get data about a character with id 1
$resourceUrl = "https://swapi.dev/api/people/1/"
$result = Get-SWAPIResource -ResourceUrl $resourceUrl

# Converting JSON Data to a PowerShell Object
$person = ConvertFrom-Json $result

# Table output
$table = @{
    Name        = $person.name
    Height      = $person.height
    Mass        = $person.mass
    HairColor   = $person.hair_color
    SkinColor   = $person.skin_color
    EyeColor    = $person.eye_color
    BirthYear   = $person.birth_year
    Gender      = $person.gender
}

Write-Host "Character data with id 1:"
$table | Format-Table -AutoSize