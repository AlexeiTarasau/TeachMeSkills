function Get-SWAPIResource {
    param(
        [Parameter(Mandatory = $true)]
        [int]$pageNumber
    )

    $resourceUrl = "https://swapi.dev/api/people/?page=$PageNumber"
        
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

# Entering a page number with characters
$pageNumber = Read-Host "Enter page number"

# Calling a function to get data about a character
$result = Get-SWAPIResource -PageNumber $pageNumber

# Converting JSON Data to a PowerShell Object
$data = ConvertFrom-Json $result

# Creating a list for data output
$characters = @()

foreach ($character in $data.results) {
    $characters += @{
        Name        = $character.name
        Height      = $character.height
        Mass        = $character.mass
        HairColor   = $character.hair_color
        SkinColor   = $character.skin_color
        EyeColor    = $character.eye_color
        BirthYear   = $character.birth_year
        Gender      = $character.gender
    }
}

# Table output
Write-Host "Character data on the page $pageNumber"
$characters | Format-Table -AutoSize